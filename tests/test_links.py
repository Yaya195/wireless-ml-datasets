from pathlib import Path

import yaml

from scripts import check_links


def test_discover_links_deduplicates_and_tracks_references(tmp_path):
    record = {
        "identity": {"canonical_url": "https://example.org/dataset"},
        "access": {"url": "https://example.org/dataset"},
        "references": [
            {"url": "https://example.org/paper", "doi": "10.1234/example"},
        ],
    }
    path = tmp_path / "dataset.yaml"
    path.write_text(yaml.safe_dump(record), encoding="utf-8")

    links, errors = check_links.discover_links([tmp_path])

    assert errors == []
    assert set(links) == {
        "https://example.org/dataset",
        "https://example.org/paper",
        "https://doi.org/10.1234/example",
    }
    assert len(links["https://example.org/dataset"]) == 2


def test_discover_links_accepts_json(tmp_path):
    path = tmp_path / "catalog.json"
    path.write_text('{"url": "https://example.org/resource"}', encoding="utf-8")

    links, errors = check_links.discover_links([path])

    assert errors == []
    assert list(links) == ["https://example.org/resource"]


def test_probe_url_accepts_success(monkeypatch):
    monkeypatch.setattr(check_links, "_request", lambda *_args, **_kwargs: (200, "https://example.org/"))

    result = check_links.probe_url("https://example.org/")

    assert result.status == "ok"
    assert result.code == 200


def test_probe_url_confirms_head_404_with_get(monkeypatch):
    calls = []

    def fake_request(_url, method, _timeout):
        calls.append(method)
        return (404, "https://example.org/missing")

    monkeypatch.setattr(check_links, "_request", fake_request)

    result = check_links.probe_url("https://example.org/missing")

    assert calls == ["HEAD", "GET"]
    assert result.status == "broken"
    assert result.code == 404


def test_probe_url_does_not_fail_on_bot_protection(monkeypatch):
    monkeypatch.setattr(check_links, "_request", lambda *_args, **_kwargs: (403, "https://example.org/"))

    result = check_links.probe_url("https://example.org/")

    assert result.status == "warning"
    assert result.code == 403


def test_probe_url_falls_back_from_head_405_to_get(monkeypatch):
    responses = iter([(405, "https://example.org/"), (200, "https://example.org/")])
    monkeypatch.setattr(check_links, "_request", lambda *_args, **_kwargs: next(responses))

    result = check_links.probe_url("https://example.org/")

    assert result.status == "ok"
    assert result.code == 200


def test_normalise_doi():
    assert check_links._normalise_doi("10.1109/EXAMPLE.2026.123") == "https://doi.org/10.1109/EXAMPLE.2026.123"
    assert check_links._normalise_doi("doi:10.1234/test") == "https://doi.org/10.1234/test"
    assert check_links._normalise_doi("") is None


def test_list_only_is_network_free(tmp_path, monkeypatch):
    path = tmp_path / "dataset.yaml"
    path.write_text("url: https://example.org/dataset\n", encoding="utf-8")

    def fail_if_called(*_args, **_kwargs):
        raise AssertionError("network should not be used")

    monkeypatch.setattr(check_links, "probe_url", fail_if_called)
    assert check_links.main([str(path), "--list-only"]) == 0


def test_bad_yaml_is_reported(tmp_path):
    path = Path(tmp_path) / "broken.yaml"
    path.write_text("a: [unterminated\n", encoding="utf-8")

    _links, errors = check_links.discover_links([path])

    assert len(errors) == 1
