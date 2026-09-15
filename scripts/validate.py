#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)

def vocabulary_map(vocab: dict, key: str) -> dict[str, str]:
    return {entry["id"]: entry["name"] for entry in vocab[key]}

def validate_repository(root: Path = ROOT) -> list[str]:
    datasets_dir = root / "data" / "datasets"
    tasks_dir = root / "data" / "tasks"
    resources_dir = root / "data" / "resources"
    collections_dir = root / "data" / "collections"
    schema_dir = root / "schema"
    vocab_path = root / "data" / "vocabularies.yaml"

    dataset_schema = json.loads(
        (schema_dir / "dataset.schema.json").read_text(encoding="utf-8")
    )
    resource_schema = json.loads(
        (schema_dir / "resource.schema.json").read_text(encoding="utf-8")
    )
    collection_schema = json.loads(
        (schema_dir / "collection.schema.json").read_text(encoding="utf-8")
    )
    dataset_validator = Draft202012Validator(
        dataset_schema, format_checker=FormatChecker()
    )
    resource_validator = Draft202012Validator(
        resource_schema, format_checker=FormatChecker()
    )
    collection_validator = Draft202012Validator(
        collection_schema, format_checker=FormatChecker()
    )
    vocab = load_yaml(vocab_path)

    task_ids = set()
    if tasks_dir.exists():
        for path in tasks_dir.glob("*.yaml"):
            item = load_yaml(path)
            task_ids.add(item["id"])

    controlled = {
        "modalities": set(vocabulary_map(vocab, "modalities")),
        "technologies": set(vocabulary_map(vocab, "technologies")),
        "generation_contexts": set(vocabulary_map(vocab, "generation_contexts")),
        "radio_configurations": set(vocabulary_map(vocab, "radio_configurations")),
        "environments": set(vocabulary_map(vocab, "environments")),
        "ground_truth": set(vocabulary_map(vocab, "ground_truth")),
        "frequency_regimes": set(vocabulary_map(vocab, "frequency_regimes")),
        "mobility_types": set(vocabulary_map(vocab, "mobility_types")),
    }

    failures: list[str] = []

    collection_ids: set[str] = set()
    for path in sorted(collections_dir.glob("*.yaml")):
        item = load_yaml(path)
        for error in sorted(
            collection_validator.iter_errors(item), key=lambda err: list(err.path)
        ):
            location = ".".join(map(str, error.path)) or "<root>"
            failures.append(
                f"{path.name}: collection schema error at {location}: {error.message}"
            )

        collection_id = item.get("id")
        if collection_id:
            if collection_id in collection_ids:
                failures.append(
                    f"{path.name}: duplicate collection id '{collection_id}'"
                )
            collection_ids.add(collection_id)
            if path.stem != collection_id:
                failures.append(
                    f"{path.name}: filename must match id '{collection_id}.yaml'"
                )

    dataset_ids: set[str] = set()
    dataset_records: list[tuple[Path, dict]] = []

    for path in sorted(datasets_dir.glob("*.yaml")):
        item = load_yaml(path)
        dataset_records.append((path, item))

        for error in sorted(dataset_validator.iter_errors(item), key=lambda err: list(err.path)):
            location = ".".join(map(str, error.path)) or "<root>"
            failures.append(f"{path.name}: schema error at {location}: {error.message}")

        dataset_id = item.get("id")
        if dataset_id:
            if dataset_id in dataset_ids:
                failures.append(f"{path.name}: duplicate dataset id '{dataset_id}'")
            dataset_ids.add(dataset_id)
            if path.stem != dataset_id:
                failures.append(f"{path.name}: filename must match id '{dataset_id}.yaml'")

        for field in (
            "modalities", "technologies", "generation_contexts",
            "radio_configurations", "environments", "ground_truth"
        ):
            for value in item.get(field, []):
                if value not in controlled[field]:
                    failures.append(f"{path.name}: unknown {field} value '{value}'")

        for value in item.get("frequency", {}).get("regimes", []):
            if value not in controlled["frequency_regimes"]:
                failures.append(f"{path.name}: unknown frequency regime '{value}'")

        for collection_id in item.get("collections", []):
            if collection_id not in collection_ids:
                failures.append(
                    f"{path.name}: unknown collection '{collection_id}'"
                )

        refs = [ref.get("id") for ref in item.get("references", [])]
        ref_set = set(refs)
        if len(refs) != len(ref_set):
            failures.append(f"{path.name}: duplicate reference id")

        for mapping in item.get("tasks", []):
            task = mapping.get("task")
            if task_ids and task not in task_ids:
                failures.append(f"{path.name}: task '{task}' does not exist in data/tasks")

            for input_name in mapping.get("inputs", []):
                if input_name not in controlled["modalities"]:
                    failures.append(
                        f"{path.name}: task '{task}' uses unknown input modality '{input_name}'"
                    )

            for target in mapping.get("targets", []):
                if target not in controlled["ground_truth"]:
                    failures.append(
                        f"{path.name}: task '{task}' uses unknown target '{target}'"
                    )

            for reference in mapping.get("evaluation_reference", []):
                if reference not in controlled["ground_truth"]:
                    failures.append(
                        f"{path.name}: task '{task}' uses unknown evaluation "
                        f"reference '{reference}'"
                    )

            context = mapping.get("context") or {}
            for environment in context.get("environments", []):
                if environment not in controlled["environments"]:
                    failures.append(
                        f"{path.name}: task '{task}' uses unknown context environment '{environment}'"
                    )
            mobility = context.get("mobility")
            if mobility is not None and mobility not in controlled["mobility_types"]:
                failures.append(
                    f"{path.name}: task '{task}' uses unknown context mobility '{mobility}'"
                )
            for regime in context.get("frequency_regimes", []):
                if regime not in controlled["frequency_regimes"]:
                    failures.append(
                        f"{path.name}: task '{task}' uses unknown context frequency regime '{regime}'"
                    )

            for ref in mapping.get("evidence", []):
                if ref not in ref_set:
                    failures.append(
                        f"{path.name}: task '{task}' references missing evidence id '{ref}'"
                    )

        for caveat in item.get("caveats", []):
            for ref in caveat.get("evidence", []):
                if ref not in ref_set:
                    failures.append(f"{path.name}: caveat references missing evidence id '{ref}'")

    resource_ids: set[str] = set()
    for path in sorted(resources_dir.glob("*.yaml")):
        item = load_yaml(path)
        for error in sorted(
            resource_validator.iter_errors(item), key=lambda err: list(err.path)
        ):
            location = ".".join(map(str, error.path)) or "<root>"
            failures.append(
                f"{path.name}: resource schema error at {location}: {error.message}"
            )

        resource_id = item.get("id")
        if resource_id:
            if resource_id in resource_ids:
                failures.append(f"{path.name}: duplicate resource id '{resource_id}'")
            resource_ids.add(resource_id)
            if path.stem != resource_id:
                failures.append(
                    f"{path.name}: filename must match id '{resource_id}.yaml'"
                )
            if resource_id in dataset_ids:
                failures.append(
                    f"{path.name}: resource id '{resource_id}' collides with a dataset id"
                )

        for collection_id in item.get("collections", []):
            if collection_id not in collection_ids:
                failures.append(
                    f"{path.name}: unknown collection '{collection_id}'"
                )

        refs = [ref.get("id") for ref in item.get("references", [])]
        ref_set = set(refs)
        if len(refs) != len(ref_set):
            failures.append(f"{path.name}: duplicate reference id")

        for mapping in item.get("task_links", []):
            task = mapping.get("task")
            if task_ids and task not in task_ids:
                failures.append(
                    f"{path.name}: task link '{task}' does not exist in data/tasks"
                )
            for ref in mapping.get("evidence", []):
                if ref not in ref_set:
                    failures.append(
                        f"{path.name}: task link '{task}' references "
                        f"missing evidence id '{ref}'"
                    )

    for path, item in dataset_records:
        relations = item.get("relations") or {}
        relation_ids = []

        if relations.get("parent"):
            relation_ids.append(("parent", relations["parent"]))

        relation_ids.extend(
            ("supersedes", value)
            for value in relations.get("supersedes", [])
        )
        relation_ids.extend(
            ("derived_from", value)
            for value in relations.get("derived_from", [])
        )

        for relation_name, target_id in relation_ids:
            if target_id == item["id"]:
                failures.append(
                    f"{path.name}: relation '{relation_name}' cannot "
                    "reference the record itself"
                )
            elif target_id not in dataset_ids:
                failures.append(
                    f"{path.name}: relation '{relation_name}' references "
                    f"unknown dataset '{target_id}'"
                )

    return failures

def main() -> int:
    failures = validate_repository()

    if failures:
        print("Validation failed:\n")
        for failure in failures:
            print(f" - {failure}")
        return 1

    dataset_count = len(list((ROOT / "data" / "datasets").glob("*.yaml")))
    resource_count = len(list((ROOT / "data" / "resources").glob("*.yaml")))
    collection_count = len(list((ROOT / "data" / "collections").glob("*.yaml")))
    print(
        "Validation passed: "
        f"{dataset_count} dataset records, "
        f"{resource_count} supporting resources, "
        f"{collection_count} collection(s)."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
