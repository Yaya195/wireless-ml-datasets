#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]

@dataclass(frozen=True)
class Finding:
    level: str
    code: str
    dataset_ids: tuple[str, ...]
    message: str

def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)

def load_datasets(root: Path):
    records = []
    for path in sorted((root / "data" / "datasets").glob("*.yaml")):
        records.append(load_yaml(path))
    return records

def normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())

def normalize_external_id(scheme: str, value: str) -> str:
    value = value.strip()
    if scheme == "doi":
        value = value.casefold()
        value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
        value = re.sub(r"^doi:\s*", "", value)
    return value.casefold()

def normalize_url(value: str) -> str:
    parts = urlsplit(value.strip())
    scheme = parts.scheme.casefold()
    # hostname = (parts.hostname or "").casefold()
    # if hostname.startswith("www."):
    #     hostname = hostname[4:]
    hostname = (parts.hostname or "").casefold()
    hostname = hostname.removeprefix("www.")

    port = parts.port
    netloc = hostname
    if port and not (
        (scheme == "http" and port == 80)
        or (scheme == "https" and port == 443)
    ):
        netloc = f"{hostname}:{port}"

    path = re.sub(r"/+$", "", parts.path) or "/"
    if hostname == "github.com" and path.endswith(".git"):
        path = path[:-4]

    return urlunsplit((scheme, netloc, path, parts.query, ""))

def relation_ids(dataset: dict) -> set[str]:
    relations = dataset.get("relations") or {}
    values = set(relations.get("supersedes", []))
    values.update(relations.get("derived_from", []))
    if relations.get("parent"):
        values.add(relations["parent"])
    return values

def are_explicitly_related(first: dict, second: dict) -> bool:
    return (
        second["id"] in relation_ids(first)
        or first["id"] in relation_ids(second)
    )

def authoritative_urls(dataset: dict) -> set[str]:
    urls = set()

    identity_url = (dataset.get("identity") or {}).get("canonical_url")
    if identity_url:
        urls.add(normalize_url(identity_url))

    access_url = (dataset.get("access") or {}).get("url")
    if access_url:
        urls.add(normalize_url(access_url))

    resources = dataset.get("official_resources") or {}
    for key in ("homepage", "repository"):
        url = resources.get(key)
        if url:
            urls.add(normalize_url(url))

    return urls

def reference_dois(dataset: dict) -> set[str]:
    values = set()
    for reference in dataset.get("references", []):
        doi = reference.get("doi")
        if doi:
            values.add(normalize_external_id("doi", doi))
    return values

def find_duplicates(records: list[dict]) -> list[Finding]:
    findings: list[Finding] = []

    canonical_urls = defaultdict(list)
    external_ids = defaultdict(list)

    for dataset in records:
        identity = dataset.get("identity") or {}

        canonical_url = identity.get("canonical_url")
        if canonical_url:
            canonical_urls[normalize_url(canonical_url)].append(dataset)

        for external_id in identity.get("external_ids", []):
            key = (
                external_id["scheme"],
                normalize_external_id(
                    external_id["scheme"],
                    external_id["value"],
                ),
            )
            external_ids[key].append(dataset)

    for url, datasets in sorted(canonical_urls.items()):
        if len(datasets) > 1:
            findings.append(Finding(
                "ERROR",
                "duplicate-canonical-url",
                tuple(sorted(dataset["id"] for dataset in datasets)),
                f"Multiple records declare the same canonical dataset URL: {url}",
            ))

    for (scheme, value), datasets in sorted(external_ids.items()):
        if len(datasets) > 1:
            findings.append(Finding(
                "ERROR",
                "duplicate-external-id",
                tuple(sorted(dataset["id"] for dataset in datasets)),
                f"Multiple records declare the same external identity {scheme}:{value}",
            ))

    name_index = defaultdict(list)
    for dataset in records:
        seen = set()
        for name in [dataset["name"], *dataset.get("aliases", [])]:
            normalized = normalize_name(name)
            if normalized and normalized not in seen:
                name_index[normalized].append(dataset)
                seen.add(normalized)

    for normalized, datasets in sorted(name_index.items()):
        unique = {dataset["id"]: dataset for dataset in datasets}
        ids = sorted(unique)

        unrelated = False
        for index, first_id in enumerate(ids):
            for second_id in ids[index + 1:]:
                if not are_explicitly_related(
                    unique[first_id],
                    unique[second_id],
                ):
                    unrelated = True

        if len(ids) > 1 and unrelated:
            findings.append(Finding(
                "WARNING",
                "name-overlap",
                tuple(ids),
                "Canonical names or aliases normalize to the same value: "
                f"{normalized}",
            ))

    for index, first in enumerate(records):
        first_urls = authoritative_urls(first)
        first_dois = reference_dois(first)

        for second in records[index + 1:]:
            if are_explicitly_related(first, second):
                continue

            shared_urls = first_urls & authoritative_urls(second)
            if shared_urls:
                findings.append(Finding(
                    "WARNING",
                    "official-url-overlap",
                    tuple(sorted((first["id"], second["id"]))),
                    "Records share authoritative/access URL(s): "
                    + ", ".join(sorted(shared_urls)),
                ))

            shared_dois = first_dois & reference_dois(second)
            if shared_dois:
                findings.append(Finding(
                    "WARNING",
                    "reference-doi-overlap",
                    tuple(sorted((first["id"], second["id"]))),
                    "Records cite the same DOI; verify that the publication "
                    "does not describe the same underlying dataset: "
                    + ", ".join(sorted(shared_dois)),
                ))

    return sorted(
        findings,
        key=lambda item: (
            0 if item.level == "ERROR" else 1,
            item.code,
            item.dataset_ids,
            item.message,
        ),
    )

def check_repository(root: Path = ROOT) -> list[Finding]:
    return find_duplicates(load_datasets(root))

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Detect duplicate or potentially duplicate dataset records."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root (defaults to current project root).",
    )
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="Return non-zero when review warnings are found.",
    )
    args = parser.parse_args()

    records = load_datasets(args.root.resolve())
    findings = find_duplicates(records)

    errors = [item for item in findings if item.level == "ERROR"]
    warnings = [item for item in findings if item.level == "WARNING"]

    for finding in findings:
        print(
            f"{finding.level} [{finding.code}] "
            f"{', '.join(finding.dataset_ids)}: {finding.message}"
        )

    if errors:
        print(
            f"Duplicate check failed: {len(records)} records, "
            f"{len(errors)} error(s), {len(warnings)} warning(s)."
        )
        return 1

    if warnings:
        print(
            f"Duplicate check passed with review warnings: "
            f"{len(records)} records, 0 errors, "
            f"{len(warnings)} warning(s)."
        )
        return 1 if args.strict_warnings else 0

    print(
        f"Duplicate check passed: {len(records)} records, "
        "0 errors, 0 warnings."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
