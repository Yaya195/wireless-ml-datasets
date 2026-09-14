"""Check external links referenced by Wireless ML Data Hub metadata.

The checker is deliberately conservative about failures:

* 2xx/3xx responses are healthy.
* 404/410 responses are treated as confirmed broken links.
* authentication, rate-limit, bot-protection, server, TLS, DNS, and timeout
  failures are reported as warnings by default because they do not prove that
  a research resource is unavailable to a normal browser.

Use ``--strict`` when every warning should also produce a non-zero exit code.
"""

from __future__ import annotations

import argparse
import json
import ssl
import sys
import time
from collections import defaultdict
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATHS = (ROOT / "data",)
USER_AGENT = (
    "Mozilla/5.0 (compatible; WirelessMLDataHub-LinkChecker/1.0; "
    "+https://github.com/)"
)

HEALTHY_CODES = range(200, 400)
RESTRICTED_CODES = {401, 403, 405, 406, 407, 409, 423, 425, 429, 451}
CONFIRMED_BROKEN_CODES = {404, 410}
HEAD_FALLBACK_CODES = {400, 404, 405, 410, 501}


@dataclass(frozen=True)
class LinkReference:
    source: str
    field: str


@dataclass(frozen=True)
class LinkResult:
    url: str
    status: str
    code: int | None
    final_url: str | None
    detail: str
    references: tuple[LinkReference, ...]


def _is_http_url(value: str) -> bool:
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _normalise_doi(value: str) -> str | None:
    doi = value.strip()
    if not doi:
        return None
    if _is_http_url(doi):
        return doi
    if doi.lower().startswith("doi:"):
        doi = doi[4:].strip()
    if doi.startswith("10.") and "/" in doi:
        return f"https://doi.org/{doi}"
    return None


def _walk_links(value: Any, source: Path, field: str = "$", key: str | None = None):
    if isinstance(value, dict):
        for child_key, child_value in value.items():
            child_field = f"{field}.{child_key}"
            yield from _walk_links(child_value, source, child_field, str(child_key))
        return

    if isinstance(value, list):
        for index, child_value in enumerate(value):
            yield from _walk_links(child_value, source, f"{field}[{index}]", key)
        return

    if not isinstance(value, str):
        return

    candidate = value.strip()
    url: str | None = None
    if _is_http_url(candidate):
        url = candidate
    elif key and key.lower() == "doi":
        url = _normalise_doi(candidate)

    if url:
        try:
            source_text = str(source.relative_to(ROOT))
        except ValueError:
            source_text = str(source)
        yield url, LinkReference(source=source_text, field=field)


def _load_structured_file(path: Path) -> Any:
    suffix = path.suffix.lower()
    with path.open("r", encoding="utf-8") as handle:
        if suffix in {".yaml", ".yml"}:
            return yaml.safe_load(handle)
        if suffix == ".json":
            return json.load(handle)
    raise ValueError(f"unsupported structured file: {path}")


def _iter_structured_files(paths: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() in {".yaml", ".yml", ".json"}:
            files.append(path)
        elif path.is_dir():
            files.extend(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file()
                and candidate.suffix.lower() in {".yaml", ".yml", ".json"}
            )
    return sorted(set(files))


def discover_links(paths: Iterable[Path]) -> tuple[dict[str, tuple[LinkReference, ...]], list[str]]:
    """Return unique URLs with all metadata references plus parse errors."""

    found: dict[str, list[LinkReference]] = defaultdict(list)
    errors: list[str] = []

    for path in _iter_structured_files(paths):
        try:
            document = _load_structured_file(path)
        except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError) as exc:
            errors.append(f"{path}: {exc}")
            continue
        for url, reference in _walk_links(document, path):
            if reference not in found[url]:
                found[url].append(reference)

    return {url: tuple(refs) for url, refs in sorted(found.items())}, errors


def _request(url: str, method: str, timeout: float) -> tuple[int, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "no-cache",
    }
    if method == "GET":
        headers["Range"] = "bytes=0-0"

    request = Request(url, headers=headers, method=method)
    try:
        with urlopen(request, timeout=timeout) as response:
            if method == "GET":
                response.read(1)
            return int(response.status), response.geturl()
    except HTTPError as exc:
        return int(exc.code), exc.geturl() or url


def _classify_http(code: int) -> tuple[str, str]:
    if code in HEALTHY_CODES:
        return "ok", f"HTTP {code}"
    if code in CONFIRMED_BROKEN_CODES:
        return "broken", f"HTTP {code}"
    if code in RESTRICTED_CODES:
        return "warning", f"HTTP {code} (restricted, rate-limited, or method-blocked)"
    if 500 <= code <= 599:
        return "warning", f"HTTP {code} (server-side failure)"
    return "warning", f"HTTP {code}"


def probe_url(
    url: str,
    references: tuple[LinkReference, ...] = (),
    *,
    timeout: float = 12.0,
    retries: int = 1,
) -> LinkResult:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return LinkResult(url, "broken", None, None, "invalid HTTP(S) URL", references)

    last_detail = "request failed"
    for attempt in range(retries + 1):
        try:
            code, final_url = _request(url, "HEAD", timeout)

            # Some research portals reject HEAD or return route-specific 404s.
            # Confirm method-sensitive and terminal-looking results with a tiny GET.
            if code in HEAD_FALLBACK_CODES:
                get_code, get_final_url = _request(url, "GET", timeout)
                code, final_url = get_code, get_final_url

            status, detail = _classify_http(code)
            if status == "warning" and code >= 500 and attempt < retries:
                last_detail = detail
                time.sleep(0.5 * (attempt + 1))
                continue
            return LinkResult(url, status, code, final_url, detail, references)

        except TimeoutError as exc:
            last_detail = f"timeout: {exc}"
        except ssl.SSLError as exc:
            last_detail = f"TLS error: {exc}"
        except URLError as exc:
            reason = getattr(exc, "reason", exc)
            last_detail = f"network error: {reason}"
        except OSError as exc:
            last_detail = f"network error: {exc}"

        if attempt < retries:
            time.sleep(0.5 * (attempt + 1))

    return LinkResult(url, "warning", None, None, last_detail, references)


def _format_references(references: tuple[LinkReference, ...], limit: int = 3) -> str:
    rendered = [f"{ref.source}:{ref.field}" for ref in references[:limit]]
    if len(references) > limit:
        rendered.append(f"+{len(references) - limit} more")
    return ", ".join(rendered)


def _write_json_report(path: Path, results: list[LinkResult], parse_errors: list[str]) -> None:
    summary = {
        "total": len(results),
        "ok": sum(result.status == "ok" for result in results),
        "warnings": sum(result.status == "warning" for result in results),
        "broken": sum(result.status == "broken" for result in results),
        "parse_errors": len(parse_errors),
    }
    payload = {
        "summary": summary,
        "parse_errors": parse_errors,
        "results": [asdict(result) for result in results],
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _resolve_paths(raw_paths: list[str] | None) -> list[Path]:
    if not raw_paths:
        return list(DEFAULT_PATHS)
    resolved: list[Path] = []
    for raw in raw_paths:
        path = Path(raw)
        if not path.is_absolute():
            path = ROOT / path
        resolved.append(path.resolve())
    return resolved


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="YAML/JSON files or directories to scan (default: data/)",
    )
    parser.add_argument("--timeout", type=float, default=12.0, help="per-request timeout in seconds")
    parser.add_argument("--retries", type=int, default=1, help="retries for transient network/server failures")
    parser.add_argument("--workers", type=int, default=8, help="maximum concurrent URL checks")
    parser.add_argument("--max-urls", type=int, default=None, help="check only the first N unique URLs")
    parser.add_argument("--strict", action="store_true", help="fail on warnings as well as confirmed broken links")
    parser.add_argument("--verbose", action="store_true", help="print healthy links too")
    parser.add_argument("--list-only", action="store_true", help="discover and list URLs without making network requests")
    parser.add_argument("--json-output", type=Path, help="write a machine-readable JSON report")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    paths = _resolve_paths(args.paths)
    links, parse_errors = discover_links(paths)

    if parse_errors:
        print("Structured-file errors:")
        for error in parse_errors:
            print(f"  ERROR {error}")
        return 2

    items = list(links.items())
    if args.max_urls is not None:
        items = items[: max(0, args.max_urls)]

    print(f"Discovered {len(items)} unique external links.")

    if args.list_only:
        for url, references in items:
            print(f"{url}  [{_format_references(references)}]")
        if args.json_output:
            listed = [
                LinkResult(url, "unchecked", None, None, "network check not requested", refs)
                for url, refs in items
            ]
            _write_json_report(args.json_output, listed, parse_errors)
        return 0

    if not items:
        if args.json_output:
            _write_json_report(args.json_output, [], parse_errors)
        return 0

    results: list[LinkResult] = []
    workers = max(1, args.workers)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                probe_url,
                url,
                references,
                timeout=max(0.1, args.timeout),
                retries=max(0, args.retries),
            ): url
            for url, references in items
        }
        for future in as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda result: (result.status != "broken", result.status != "warning", result.url))

    for result in results:
        if result.status == "ok" and not args.verbose:
            continue
        label = result.status.upper()
        refs = _format_references(result.references)
        redirect = ""
        if result.final_url and result.final_url.rstrip("/") != result.url.rstrip("/"):
            redirect = f" -> {result.final_url}"
        print(f"{label:7} {result.url}{redirect} :: {result.detail}")
        if refs:
            print(f"        referenced by {refs}")

    ok_count = sum(result.status == "ok" for result in results)
    warning_count = sum(result.status == "warning" for result in results)
    broken_count = sum(result.status == "broken" for result in results)
    print(
        "Link check summary: "
        f"{len(results)} checked, {ok_count} healthy, "
        f"{warning_count} warnings, {broken_count} confirmed broken."
    )

    if args.json_output:
        output_path = args.json_output
        if not output_path.is_absolute():
            output_path = ROOT / output_path
        _write_json_report(output_path, results, parse_errors)
        print(f"Report written to {output_path}")

    if broken_count:
        return 1
    if args.strict and warning_count:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
