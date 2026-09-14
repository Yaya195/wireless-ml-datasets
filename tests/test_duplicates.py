from scripts.check_duplicates import find_duplicates


def record(
    dataset_id,
    name,
    *,
    aliases=None,
    canonical_url=None,
    external_ids=None,
    access_url=None,
    homepage=None,
    repository=None,
    reference_dois=None,
    relations=None,
):
    return {
        "id": dataset_id,
        "name": name,
        "aliases": aliases or [],
        "identity": {
            "canonical_url": canonical_url,
            "version": None,
            "external_ids": external_ids or [],
        },
        "access": {"url": access_url},
        "official_resources": {
            "homepage": homepage,
            "repository": repository,
        },
        "references": [
            {"doi": doi}
            for doi in (reference_dois or [])
        ],
        "relations": relations or {},
    }

def finding_codes(findings):
    return {(item.level, item.code) for item in findings}

def test_same_external_identity_is_hard_error():
    records = [
        record(
            "a",
            "Dataset A",
            external_ids=[
                {"scheme": "doi", "value": "10.1234/ABC"},
            ],
        ),
        record(
            "b",
            "Dataset B",
            external_ids=[
                {
                    "scheme": "doi",
                    "value": "https://doi.org/10.1234/abc",
                },
            ],
        ),
    ]

    assert (
        "ERROR",
        "duplicate-external-id",
    ) in finding_codes(find_duplicates(records))

def test_same_canonical_url_is_hard_error():
    records = [
        record(
            "a",
            "Dataset A",
            canonical_url="https://example.org/data/",
        ),
        record(
            "b",
            "Dataset B",
            canonical_url="https://www.example.org/data",
        ),
    ]

    assert (
        "ERROR",
        "duplicate-canonical-url",
    ) in finding_codes(find_duplicates(records))

def test_name_alias_overlap_is_warning():
    records = [
        record("a", "Deep Sense 6G"),
        record("b", "Other Name", aliases=["DeepSense6G"]),
    ]

    assert (
        "WARNING",
        "name-overlap",
    ) in finding_codes(find_duplicates(records))

def test_shared_reference_doi_is_warning_not_error():
    records = [
        record(
            "a",
            "Dataset A",
            reference_dois=["10.1000/test"],
        ),
        record(
            "b",
            "Dataset B",
            reference_dois=["10.1000/TEST"],
        ),
    ]

    findings = find_duplicates(records)

    assert (
        "WARNING",
        "reference-doi-overlap",
    ) in finding_codes(findings)
    assert not any(item.level == "ERROR" for item in findings)

def test_explicit_relation_suppresses_probable_name_warning():
    records = [
        record("a", "Dataset"),
        record(
            "b",
            "Dataset",
            relations={"supersedes": ["a"]},
        ),
    ]

    assert (
        "WARNING",
        "name-overlap",
    ) not in finding_codes(find_duplicates(records))
