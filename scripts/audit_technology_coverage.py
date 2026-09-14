#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Candidate:
    dataset_id: str
    reason: str


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def searchable_text(dataset: dict) -> str:
    parts: list[str] = [
        str(dataset.get("name", "")),
        str(dataset.get("description", "")),
    ]
    parts.extend(str(alias) for alias in dataset.get("aliases", []))

    for ref in dataset.get("references", []):
        parts.extend(
            str(value)
            for value in (ref.get("title"), ref.get("url"), ref.get("notes"))
            if value
        )

    for value in (dataset.get("official_resources") or {}).values():
        if value:
            parts.append(str(value))

    return " ".join(parts).lower()


def audit_repository(root: Path = ROOT) -> tuple[list[Candidate], dict[str, int], list[str]]:
    vocab = load_yaml(root / "data" / "vocabularies.yaml")
    technology_ids = {entry["id"] for entry in vocab.get("technologies", [])}
    vocabulary_problems: list[str] = []

    if "6g" not in technology_ids:
        vocabulary_problems.append("technology vocabulary is missing first-class '6g'")
    if "lorawan" not in technology_ids:
        vocabulary_problems.append("technology vocabulary is missing 'lorawan'")
    for forbidden in ("lora", "isac"):
        if forbidden in technology_ids:
            vocabulary_problems.append(
                f"technology vocabulary must not contain '{forbidden}'"
            )

    counts = {technology_id: 0 for technology_id in sorted(technology_ids)}
    candidates: list[Candidate] = []

    for path in sorted((root / "data" / "datasets").glob("*.yaml")):
        dataset = load_yaml(path)
        dataset_id = dataset["id"]
        technologies = set(dataset.get("technologies", []))
        generations = set(dataset.get("generation_contexts", []))

        for technology_id in technologies:
            counts[technology_id] = counts.get(technology_id, 0) + 1

        if ("6g" in technologies) != ("6g" in generations):
            candidates.append(
                Candidate(
                    dataset_id,
                    "6g technology and 6g generation context are inconsistent",
                )
            )
            continue

        text = searchable_text(dataset)
        if "6g" in text and "6g" not in technologies:
            candidates.append(
                Candidate(
                    dataset_id,
                    "record contains an explicit 6G signal but lacks technology '6g'; verify the authoritative source",
                )
            )

    return candidates, counts, vocabulary_problems


def main() -> int:
    candidates, counts, vocabulary_problems = audit_repository()

    if vocabulary_problems:
        print("Technology vocabulary audit failed:\n")
        for problem in vocabulary_problems:
            print(f" - {problem}")
        return 1

    print(
        f"Technology-coverage audit: {len(candidates)} candidate mapping(s) require review."
    )
    print(f"6G-tagged core datasets: {counts.get('6g', 0)}")

    if candidates:
        print()
        for candidate in candidates:
            print(f" - {candidate.dataset_id}: {candidate.reason}")
        print()
        print(
            "This audit never modifies dataset records. Verify authoritative evidence "
            "before adding or removing a technology tag."
        )
        return 1

    print()
    print(
        "This audit never modifies dataset records. Verify authoritative evidence "
        "before adding or removing a technology tag."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
