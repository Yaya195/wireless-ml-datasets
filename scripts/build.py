#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
GENERATED_NOTICE = "<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->\n"

GENERATED_FILE_PATHS = (
    "catalog/README.md",
    "catalog/datasets.md",
    "catalog/resources.md",
    "catalog/technologies.md",
    "dist/catalog.json",
)

GENERATED_DIRECTORY_PATHS = (
    "catalog/tasks",
    "catalog/datasets",
    "catalog/collections",
    "catalog/technologies",
)


DEFAULT_COMPARISON_FIELDS = [
    "inputs",
    "targets",
    "origin",
    "environments",
    "mobility",
    "access",
]

SCALE_LABELS = {
    "samples": "Samples",
    "sequences": "Sequences",
    "scenarios": "Scenarios",
    "participants": "Participants",
    "devices": "Devices",
    "sites": "Sites",
    "duration_hours": "Duration (hours)",
    "size_gb": "Size (GB)",
}

FIELD_LABELS = {
    "inputs": "Inputs",
    "targets": "Targets",
    "evaluation-reference": "Evaluation reference",
    "origin": "Origin",
    "frequency-regimes": "Frequency",
    "environments": "Environment",
    "mobility": "Mobility",
    "access": "Access",
    "temporal-structure": "Temporal structure",
    "scale-samples": "Samples",
    "scale-participants": "Participants",
}

def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)

def load_tasks(root: Path):
    tasks = {}
    for path in sorted((root / "data" / "tasks").glob("*.yaml")):
        item = load_yaml(path)
        tasks[item["id"]] = item
    return tasks

def load_categories(root: Path):
    data = load_yaml(root / "data" / "task-categories.yaml")
    return {item["id"]: item for item in data["categories"]}

def load_datasets(root: Path):
    items = {}
    for path in sorted((root / "data" / "datasets").glob("*.yaml")):
        item = load_yaml(path)
        items[item["id"]] = item
    return items

def load_resources(root: Path):
    items = {}
    resources_dir = root / "data" / "resources"
    if not resources_dir.exists():
        return items
    for path in sorted(resources_dir.glob("*.yaml")):
        item = load_yaml(path)
        items[item["id"]] = item
    return items

def load_collections(root: Path):
    items = {}
    collections_dir = root / "data" / "collections"
    if not collections_dir.exists():
        return items
    for path in sorted(collections_dir.glob("*.yaml")):
        item = load_yaml(path)
        items[item["id"]] = item
    return items

def load_vocabularies(root: Path):
    data = load_yaml(root / "data" / "vocabularies.yaml")
    return data, {
        key: {entry["id"]: entry["name"] for entry in value}
        for key, value in data.items()
        if isinstance(value, list) and all(isinstance(entry, dict) and "id" in entry for entry in value)
    }

def humanize_slug(value: str) -> str:
    return value.replace("-", " ").replace("_", " ").title()

def label(value, labels, vocab_name=None):
    if value is None:
        return "—"
    if vocab_name and value in labels.get(vocab_name, {}):
        return labels[vocab_name][value]
    return humanize_slug(str(value))

def label_list(values, labels, vocab_name=None):
    if not values:
        return "—"
    return ", ".join(label(value, labels, vocab_name) for value in values)

def md_link(text, target):
    return f"[{text}]({target})"

def task_matches(task_id, datasets):
    matches = []
    for dataset in datasets.values():
        for mapping in dataset.get("tasks", []):
            if mapping["task"] == task_id:
                matches.append((dataset, mapping))
    return matches

def task_resource_matches(task_id, resources):
    matches = []
    for resource in resources.values():
        for mapping in resource.get("task_links", []):
            if mapping["task"] == task_id:
                matches.append((resource, mapping))
    return matches

def technology_matches(technology_id, datasets):
    return [
        dataset
        for dataset in datasets.values()
        if technology_id in dataset.get("technologies", [])
    ]

RESOURCE_KIND_LABELS = {
    "benchmark-dataset": "Benchmark dataset",
    "benchmark-suite": "Benchmark suite",
    "benchmark-framework": "Benchmark framework",
    "benchmark-platform": "Benchmark platform",
    "data-portal": "Data portal",
    "dataset-collection": "Dataset collection",
}

def resource_kind_label(value):
    return RESOURCE_KIND_LABELS.get(value, humanize_slug(value))

def mapping_context_value(dataset, mapping, field):
    context = mapping.get("context") or {}

    if field == "environments":
        return context.get("environments", dataset.get("environments", []))
    if field == "mobility":
        return context.get("mobility", dataset.get("mobility", {}).get("type"))
    if field == "frequency-regimes":
        return context.get("frequency_regimes", dataset.get("frequency", {}).get("regimes", []))

    return None

def render_comparison_value(field, dataset, mapping, labels):
    if field == "inputs":
        return label_list(mapping.get("inputs", []), labels, "modalities")
    if field == "targets":
        return label_list(mapping.get("targets", []), labels, "ground_truth")
    if field == "evaluation-reference":
        return label_list(
            mapping.get("evaluation_reference", []),
            labels,
            "ground_truth",
        )
    if field == "origin":
        return label(dataset["origin"]["type"], labels, "origins")
    if field == "frequency-regimes":
        return label_list(mapping_context_value(dataset, mapping, field), labels, "frequency_regimes")
    if field == "environments":
        return label_list(mapping_context_value(dataset, mapping, field), labels, "environments")
    if field == "mobility":
        return label(mapping_context_value(dataset, mapping, field), labels, "mobility_types")
    if field == "access":
        return label(dataset["access"]["status"], labels, "access_statuses")
    if field == "temporal-structure":
        return label(dataset["temporal_structure"], labels, "temporal_structures")
    if field == "scale-samples":
        value = (dataset.get("scale") or {}).get("samples")
        return f"{value:,}" if isinstance(value, int) else "—"
    if field == "scale-participants":
        value = (dataset.get("scale") or {}).get("participants")
        return f"{value:,}" if isinstance(value, int) else "—"
    return "—"

def task_dataset_label(dataset, labels):
    name = md_link(dataset["name"], f"../datasets/{dataset['id']}.md")
    resource_type = dataset.get("resource_type", "dataset")
    if resource_type == "dataset":
        return name

    short_labels = {
        "dataset-family": "Family",
        "dataset-collection": "Collection",
    }
    badge = short_labels.get(
        resource_type,
        label(resource_type, labels, "resource_types"),
    )
    return f"{name}<br><sub>{badge}</sub>"

def render_task_page(task, matches, labels, resources=None):
    fields = task.get("comparison_fields") or DEFAULT_COMPARISON_FIELDS

    lines = [
        GENERATED_NOTICE.rstrip(),
        "",
        f"# {task['name']}",
        "",
        task["description"],
        "",
    ]

    if task.get("aliases"):
        lines += [f"**Aliases:** {', '.join(task['aliases'])}", ""]

    lines += [f"**Datasets in catalogue:** {len(matches)}", ""]

    headers = ["Dataset"] + [FIELD_LABELS[field] for field in fields]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")

    for dataset, mapping in sorted(matches, key=lambda pair: pair[0]["name"].lower()):
        row = [task_dataset_label(dataset, labels)]
        row.extend(render_comparison_value(field, dataset, mapping, labels) for field in fields)
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    supporting = task_resource_matches(task["id"], resources or {})
    if supporting:
        lines += [
            "## Related supporting resources",
            "",
            "These benchmarks or platforms are related to the task but are not counted as core dataset mappings above.",
            "",
        ]
        for resource, mapping in sorted(
            supporting, key=lambda pair: pair[0]["name"].lower()
        ):
            lines.append(
                f"- [{resource['name']}]({resource['url']}) — {mapping['scope']}"
            )
        lines.append("")

    return "\n".join(lines)

def deduplicated_resources(dataset):
    candidates = []
    if dataset.get("access", {}).get("url"):
        candidates.append(("Dataset access", dataset["access"]["url"]))

    resources = dataset.get("official_resources", {})
    for key, title in [
        ("homepage", "Official homepage"),
        ("repository", "Official repository"),
        ("documentation", "Documentation"),
        ("loader", "Loader / access tooling"),
    ]:
        if resources.get(key):
            candidates.append((title, resources[key]))

    seen = set()
    result = []
    for title, url in candidates:
        if url in seen:
            continue
        seen.add(url)
        result.append((title, url))
    return result

def render_dataset_page(dataset, tasks, labels, collections=None):
    lines = [GENERATED_NOTICE.rstrip(), "", f"# {dataset['name']}", ""]

    if dataset.get("aliases"):
        lines += [f"**Aliases:** {', '.join(dataset['aliases'])}", ""]

    lines += [
        dataset["description"],
        "",
        "## Overview",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Resource type | {label(dataset['resource_type'], labels, 'resource_types')} |",
        f"| Origin | {label(dataset['origin']['type'], labels, 'origins')} |",
        f"| Modalities | {label_list(dataset.get('modalities', []), labels, 'modalities')} |",
        f"| Technologies | {label_list(dataset.get('technologies', []), labels, 'technologies')} |",
        f"| Generation context | {label_list(dataset.get('generation_contexts', []), labels, 'generation_contexts')} |",
        f"| Radio configuration | {label_list(dataset.get('radio_configurations', []), labels, 'radio_configurations')} |",
        f"| Environment | {label_list(dataset.get('environments', []), labels, 'environments')} |",
        f"| Mobility | {label(dataset['mobility']['type'], labels, 'mobility_types')} |",
        f"| Temporal structure | {label(dataset['temporal_structure'], labels, 'temporal_structures')} |",
        f"| Access | {label(dataset['access']['status'], labels, 'access_statuses')} |",
        f"| License | {dataset['license']['name'] or humanize_slug(dataset['license']['status'])} |",
    ]

    collection_links = []
    for collection_id in dataset.get("collections", []):
        collection = (collections or {}).get(collection_id)
        collection_name = collection["name"] if collection else humanize_slug(collection_id)
        collection_links.append(
            md_link(collection_name, f"../collections/{collection_id}.md")
        )
    if collection_links:
        lines.append(f"| Collection(s) | {' · '.join(collection_links)} |")
    lines.append("")

    freq = dataset.get("frequency", {})
    lines += ["## Frequency", ""]
    if freq.get("regimes"):
        lines.append(f"**Regimes:** {label_list(freq['regimes'], labels, 'frequency_regimes')}")
    if freq.get("bands"):
        lines.append(f"**Bands:** {', '.join(band['label'] for band in freq['bands'])}")
    if not freq.get("regimes") and not freq.get("bands"):
        lines.append(f"**Status:** {humanize_slug(freq.get('status', 'unknown'))}")
    if freq.get("notes"):
        lines += ["", freq["notes"]]
    lines.append("")

    lines += ["## Supported wireless tasks", ""]
    for mapping in dataset.get("tasks", []):
        task = tasks.get(mapping["task"], {"name": humanize_slug(mapping["task"])})
        task_name = md_link(task["name"], f"../tasks/{mapping['task']}.md")
        lines += [
            f"### {task_name}",
            "",
            f"**Inputs:** {label_list(mapping.get('inputs', []), labels, 'modalities')}",
            "",
            f"**Targets:** {label_list(mapping.get('targets', []), labels, 'ground_truth')}",
            "",
        ]
        if mapping.get("evaluation_reference"):
            lines += [
                "**Evaluation reference:** "
                + label_list(
                    mapping["evaluation_reference"],
                    labels,
                    "ground_truth",
                ),
                "",
            ]
        if mapping.get("scope"):
            lines += [f"**Scope:** {mapping['scope']}", ""]
        context = mapping.get("context") or {}
        context_parts = []
        if context.get("environments"):
            context_parts.append(
                f"Environment: {label_list(context['environments'], labels, 'environments')}"
            )
        if context.get("mobility"):
            context_parts.append(
                f"Mobility: {label(context['mobility'], labels, 'mobility_types')}"
            )
        if context.get("frequency_regimes"):
            context_parts.append(
                f"Frequency: {label_list(context['frequency_regimes'], labels, 'frequency_regimes')}"
            )
        if context_parts:
            lines += [f"**Task context:** {' · '.join(context_parts)}", ""]
        if mapping.get("notes"):
            lines += [mapping["notes"], ""]

    scale = dataset.get("scale", {})
    nonempty_scale = [
        (key, value)
        for key, value in scale.items()
        if key != "notes" and value is not None
    ]
    if nonempty_scale or scale.get("notes"):
        lines += ["## Scale", ""]
        for key, value in nonempty_scale:
            formatted = f"{value:,}" if isinstance(value, int) else value
            scale_label = SCALE_LABELS.get(key, humanize_slug(key))
            lines.append(f"- **{scale_label}:** {formatted}")
        if scale.get("notes"):
            lines.append(f"- **Notes:** {scale['notes']}")
        lines.append("")

    resources = deduplicated_resources(dataset)
    if resources:
        lines += ["## Resources", ""]
        for title, url in resources:
            lines.append(f"- {md_link(title, url)}")
        lines.append("")

    if dataset.get("caveats"):
        lines += ["## Caveats", ""]
        for caveat in dataset["caveats"]:
            lines.append(f"- {caveat['text']}")
        lines.append("")

    lines += ["## References", ""]
    for ref in dataset["references"]:
        title = ref.get("title") or ref["url"]
        lines.append(f"- {md_link(title, ref['url'])}")
    lines.append("")

    verification = dataset.get("verification", {})
    lines += [
        "## Metadata verification",
        "",
        f"**Status:** {label(dataset['status'], labels, 'metadata_statuses')}",
        "",
        f"**Last checked:** `{verification.get('last_checked', 'unknown')}`",
        "",
    ]
    if verification.get("notes"):
        lines += [verification["notes"], ""]

    return "\n".join(lines).rstrip() + "\n"

STATS_START = "<!-- CATALOG_STATS_START -->"
STATS_END = "<!-- CATALOG_STATS_END -->"
FEATURED_START = "<!-- FEATURED_DATASETS_START -->"
FEATURED_END = "<!-- FEATURED_DATASETS_END -->"


def render_catalog_stats(datasets, tasks, resources=None):
    populated_task_ids = {
        mapping["task"]
        for dataset in datasets.values()
        for mapping in dataset.get("tasks", [])
    }
    populated = sum(
        1
        for task_id in populated_task_ids
        if tasks.get(task_id, {}).get("status") == "active"
    )
    return "\n".join([
        STATS_START,
        "<!-- Generated by scripts/build.py — do not edit this block manually. -->",
        "",
        f"**Catalogue:** **{len(datasets)} datasets** across **{populated} populated wireless tasks**.",
        f"**Supporting resources:** **{len(resources or {})} curated benchmark, foundation-model, and discovery resources**.",
        "",
        STATS_END,
    ])

def update_readme_stats(root, datasets, tasks, resources=None):
    readme_path = root / "README.md"
    if not readme_path.exists():
        return
    text = readme_path.read_text(encoding="utf-8")
    if STATS_START not in text or STATS_END not in text:
        raise ValueError("README.md is missing CATALOG_STATS_START/END markers.")
    before, remainder = text.split(STATS_START, 1)
    _, after = remainder.split(STATS_END, 1)
    readme_path.write_text(
        before + render_catalog_stats(datasets, tasks, resources) + after,
        encoding="utf-8",
    )

def render_featured_datasets(datasets, tasks, labels):
    featured = sorted(
        [dataset for dataset in datasets.values() if dataset.get("featured")],
        key=lambda item: item["name"].lower(),
    )

    lines = [
        FEATURED_START,
        "<!-- Generated by scripts/build.py — do not edit this block manually. -->",
        "",
        "| Dataset | Representative task(s) | Origin | Access |",
        "|---|---|---|---|",
    ]

    for dataset in featured:
        dataset_link = md_link(
            dataset["name"],
            f"catalog/datasets/{dataset['id']}.md",
        )

        mappings = dataset.get("tasks", [])
        task_links = []
        for mapping in mappings[:3]:
            task = tasks.get(mapping["task"])
            task_name = task["name"] if task else humanize_slug(mapping["task"])
            task_links.append(
                md_link(task_name, f"catalog/tasks/{mapping['task']}.md")
            )

        if len(mappings) > 3:
            task_links.append(f"+{len(mappings) - 3} more")

        lines.append(
            f"| {dataset_link} | {' · '.join(task_links)} | "
            f"{label(dataset['origin']['type'], labels, 'origins')} | "
            f"{label(dataset['access']['status'], labels, 'access_statuses')} |"
        )

    lines += ["", FEATURED_END]
    return "\n".join(lines)

def update_readme_featured(root, datasets, tasks, labels):
    readme_path = root / "README.md"

    # build() is also used by unit tests and downstream tooling with a minimal
    # repository containing only data/. README enrichment is optional there.
    if not readme_path.exists():
        return

    text = readme_path.read_text(encoding="utf-8")
    if FEATURED_START not in text or FEATURED_END not in text:
        raise ValueError(
            "README.md is missing FEATURED_DATASETS_START/END markers."
        )

    before, remainder = text.split(FEATURED_START, 1)
    _, after = remainder.split(FEATURED_END, 1)

    readme_path.write_text(
        before + render_featured_datasets(datasets, tasks, labels) + after,
        encoding="utf-8",
    )

def render_catalog_home(categories, tasks, datasets, collections=None, resources=None):
    populated = {}
    for task in tasks.values():
        matches = task_matches(task["id"], datasets)
        if task.get("status") == "active" and matches:
            populated[task["id"]] = (task, matches)

    lines = [
        GENERATED_NOTICE.rstrip(),
        "",
        "# Browse by wireless research task",
        "",
        "Start from the wireless problem you want to study, then compare the curated datasets that support it.",
        "",
        f"**Datasets:** {len(datasets)} · **Populated tasks:** {len(populated)}",
        "",
        "[Browse all datasets](datasets.md) · [Browse by wireless technology](technologies.md) · [Supporting resources](resources.md) · [Machine-readable catalogue](../dist/catalog.json)",
        "",
    ]

    for category in sorted(categories.values(), key=lambda item: item.get("order", 9999)):
        category_tasks = [
            (task, matches)
            for task, matches in populated.values()
            if task.get("category") == category["id"]
        ]
        if not category_tasks:
            continue

        lines += [
            f"## {category['name']}",
            "",
            category["description"],
            "",
        ]

        for task, matches in sorted(category_tasks, key=lambda pair: pair[0]["name"].lower()):
            count = len(matches)
            noun = "dataset" if count == 1 else "datasets"
            lines.append(
                f"- [{task['name']}](tasks/{task['id']}.md) — {count} {noun}"
            )

        lines.append("")

    active_collections = [
        item for item in (collections or {}).values() if item.get("status") == "active"
    ]
    if active_collections:
        lines += ["## Cross-cutting collections", ""]
        for collection in sorted(active_collections, key=lambda item: item["name"].lower()):
            lines.append(
                f"- [{collection['name']}](collections/{collection['id']}.md) — {collection['description']}"
            )
        lines.append("")

    lines += [
        "## About the catalogue",
        "",
        "Task pages compare datasets using task-relevant metadata. Dataset pages provide provenance, access, licensing, task evidence, caveats, and verification information.",
        "",
        "The catalogue is generated from structured YAML under `data/`; do not edit generated files directly.",
        "",
    ]

    return "\n".join(lines)

def render_dataset_index(datasets, tasks, labels):
    lines = [
        GENERATED_NOTICE.rstrip(),
        "",
        "# All datasets",
        "",
        f"Datasets in catalogue: **{len(datasets)}**",
        "",
        "| Dataset | Wireless tasks | Data | Origin | Environment | Access |",
        "|---|---|---|---|---|---|",
    ]

    for dataset in sorted(datasets.values(), key=lambda item: item["name"].lower()):
        name = md_link(dataset["name"], f"datasets/{dataset['id']}.md")
        task_links = []
        for mapping in dataset.get("tasks", []):
            task = tasks.get(mapping["task"])
            task_name = task["name"] if task else humanize_slug(mapping["task"])
            task_links.append(md_link(task_name, f"tasks/{mapping['task']}.md"))

        lines.append(
            f"| {name} | {' · '.join(task_links)} | "
            f"{label_list(dataset.get('modalities', []), labels, 'modalities')} | "
            f"{label(dataset['origin']['type'], labels, 'origins')} | "
            f"{label_list(dataset.get('environments', []), labels, 'environments')} | "
            f"{label(dataset['access']['status'], labels, 'access_statuses')} |"
        )

    lines.append("")
    return "\n".join(lines)

def render_technology_index(datasets, labels):
    used = []
    for technology_id, technology_name in labels.get("technologies", {}).items():
        matches = technology_matches(technology_id, datasets)
        if matches:
            used.append((technology_id, technology_name, matches))

    lines = [
        GENERATED_NOTICE.rstrip(),
        "",
        "# Browse by wireless technology",
        "",
        "Technology is a secondary discovery axis; wireless research task remains the primary organization of the catalogue.",
        "",
        "| Technology | Core datasets |",
        "|---|---:|",
    ]
    for technology_id, technology_name, matches in sorted(
        used, key=lambda item: item[1].lower()
    ):
        lines.append(
            f"| [{technology_name}](technologies/{technology_id}.md) | {len(matches)} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_technology_page(technology_id, technology_name, matches, tasks, labels):
    lines = [
        GENERATED_NOTICE.rstrip(),
        "",
        f"# {technology_name}",
        "",
        f"Core datasets tagged with **{technology_name}**: **{len(matches)}**",
        "",
        "Technology tags support secondary discovery and filtering. Dataset↔Task mappings remain the evidence-backed primary organization.",
        "",
        "| Dataset | Wireless tasks | Origin | Frequency | Access |",
        "|---|---|---|---|---|",
    ]
    for dataset in sorted(matches, key=lambda item: item["name"].lower()):
        task_links = []
        for mapping in dataset.get("tasks", []):
            task = tasks.get(mapping["task"])
            task_name = task["name"] if task else humanize_slug(mapping["task"])
            task_links.append(f"[{task_name}](../tasks/{mapping['task']}.md)")
        lines.append(
            f"| [{dataset['name']}](../datasets/{dataset['id']}.md) | "
            f"{' · '.join(task_links)} | "
            f"{label(dataset['origin']['type'], labels, 'origins')} | "
            f"{label_list(dataset.get('frequency', {}).get('regimes', []), labels, 'frequency_regimes')} | "
            f"{label(dataset['access']['status'], labels, 'access_statuses')} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_resource_index(resources, collections):
    lines = [
        GENERATED_NOTICE.rstrip(),
        "",
        "# Supporting benchmarks & discovery resources",
        "",
        "These resources complement the task-mapped dataset catalogue. They are curated to help users run established benchmarks or continue a personalized dataset search; they are not included in the core dataset count.",
        "",
        f"Supporting resources: **{len(resources)}**",
        "",
    ]

    active_collections = [
        item for item in collections.values() if item.get("status") == "active"
    ]
    if active_collections:
        lines += ["## Cross-cutting collections", ""]
        for collection in sorted(active_collections, key=lambda item: item["name"].lower()):
            lines.append(
                f"- [{collection['name']}](collections/{collection['id']}.md) — {collection['description']}"
            )
        lines.append("")

    groups = [
        (
            "Benchmark datasets, suites & frameworks",
            {"benchmark-dataset", "benchmark-suite", "benchmark-framework", "benchmark-platform"},
        ),
        (
            "Dataset portals & collections",
            {"data-portal", "dataset-collection"},
        ),
    ]

    for title, kinds in groups:
        group = [r for r in resources.values() if r["resource_kind"] in kinds]
        if not group:
            continue
        lines += [f"## {title}", "", "| Resource | Type | Focus | Access | How to use |", "|---|---|---|---|---|"]
        for resource in sorted(group, key=lambda item: item["name"].lower()):
            guidance = resource.get("search_guidance") or "—"
            lines.append(
                f"| [{resource['name']}]({resource['url']}) | {resource_kind_label(resource['resource_kind'])} | "
                f"{humanize_slug(resource['wireless_relevance'])} | {humanize_slug(resource['access'])} | {guidance} |"
            )
        lines.append("")

    return "\n".join(lines)


def render_collection_page(collection, datasets, resources, tasks):
    dataset_members = [
        d for d in datasets.values() if collection["id"] in d.get("collections", [])
    ]
    resource_members = [
        r for r in resources.values() if collection["id"] in r.get("collections", [])
    ]

    lines = [
        GENERATED_NOTICE.rstrip(),
        "",
        f"# {collection['name']}",
        "",
        collection["description"],
        "",
        collection["scope"],
        "",
        f"**Core task-mapped datasets in this collection:** {len(dataset_members)}  ",
        f"**Supporting resources in this collection:** {len(resource_members)}",
        "",
    ]

    if dataset_members:
        lines += ["## Core datasets", "", "| Dataset | Wireless tasks |", "|---|---|"]
        for dataset in sorted(dataset_members, key=lambda item: item["name"].lower()):
            task_links = []
            for mapping in dataset.get("tasks", []):
                task = tasks.get(mapping["task"])
                task_name = task["name"] if task else humanize_slug(mapping["task"])
                task_links.append(f"[{task_name}](../tasks/{mapping['task']}.md)")
            lines.append(
                f"| [{dataset['name']}](../datasets/{dataset['id']}.md) | {' · '.join(task_links)} |"
            )
        lines.append("")

    if resource_members:
        lines += ["## Supporting resources", "", "| Resource | Type | Related wireless task(s) |", "|---|---|---|"]
        for resource in sorted(resource_members, key=lambda item: item["name"].lower()):
            task_names = []
            for link in resource.get("task_links", []):
                task = tasks.get(link["task"])
                task_names.append(task["name"] if task else humanize_slug(link["task"]))
            lines.append(
                f"| [{resource['name']}]({resource['url']}) | {resource_kind_label(resource['resource_kind'])} | "
                f"{', '.join(task_names) if task_names else 'Cross-cutting telecom reasoning / evaluation'} |"
            )
        lines.append("")

    if collection.get("notes"):
        lines += ["## Notes", "", collection["notes"], ""]

    return "\n".join(lines)


def render_catalog_json(tasks, categories, datasets, vocabularies, collections=None, resources=None):
    populated_task_ids = {
        mapping["task"]
        for dataset in datasets.values()
        for mapping in dataset.get("tasks", [])
    }

    return {
        "schema_version": "0.5",
        "categories": sorted(categories.values(), key=lambda item: item.get("order", 9999)),
        "tasks": sorted(
            [task for task in tasks.values() if task["id"] in populated_task_ids],
            key=lambda item: item["id"],
        ),
        "datasets": sorted(datasets.values(), key=lambda item: item["id"]),
        "collections": sorted((collections or {}).values(), key=lambda item: item["id"]),
        "resources": sorted((resources or {}).values(), key=lambda item: item["id"]),
        "technology_index": [
            {
                "id": entry["id"],
                "name": entry["name"],
                "dataset_count": len(technology_matches(entry["id"], datasets)),
                "dataset_ids": sorted(
                    dataset["id"]
                    for dataset in technology_matches(entry["id"], datasets)
                ),
            }
            for entry in vocabularies.get("technologies", [])
            if technology_matches(entry["id"], datasets)
        ],
        "vocabularies": vocabularies,
    }

def generated_output_files(root: Path):
    files = []

    for relative in GENERATED_FILE_PATHS:
        path = root / relative
        if path.exists():
            files.append(path)

    for relative in GENERATED_DIRECTORY_PATHS:
        directory = root / relative
        if directory.exists():
            files.extend(path for path in directory.rglob("*") if path.is_file())

    # README.md is partly generated: catalogue stats and Featured datasets blocks
    # are rewritten, and their consistency is protected by --check.
    readme = root / "README.md"
    if readme.exists():
        files.append(readme)

    return sorted(set(files))

def check_generated(root: Path = ROOT):
    root = root.resolve()

    with tempfile.TemporaryDirectory(prefix="ml4wirelesscom-build-check-") as tmp:
        temp_root = Path(tmp)

        shutil.copytree(root / "data", temp_root / "data")
        if (root / "README.md").exists():
            shutil.copy2(root / "README.md", temp_root / "README.md")
        build(temp_root)

        expected_files = {
            str(path.relative_to(temp_root)): path.read_bytes()
            for path in generated_output_files(temp_root)
        }
        actual_files = {
            str(path.relative_to(root)): path.read_bytes()
            for path in generated_output_files(root)
        }

    problems = []

    missing = sorted(set(expected_files) - set(actual_files))
    extra = sorted(set(actual_files) - set(expected_files))
    changed = sorted(
        relative
        for relative in set(expected_files) & set(actual_files)
        if expected_files[relative] != actual_files[relative]
    )

    problems.extend(f"missing generated file: {path}" for path in missing)
    problems.extend(f"stale/extra generated file: {path}" for path in extra)
    problems.extend(f"stale generated file: {path}" for path in changed)

    return problems

def build(root: Path = ROOT):
    tasks = load_tasks(root)
    categories = load_categories(root)
    datasets = load_datasets(root)
    resources = load_resources(root)
    collections = load_collections(root)
    vocabularies, labels = load_vocabularies(root)

    task_dir = root / "catalog" / "tasks"
    dataset_dir = root / "catalog" / "datasets"
    collection_dir = root / "catalog" / "collections"
    technology_dir = root / "catalog" / "technologies"
    dist_dir = root / "dist"

    task_dir.mkdir(parents=True, exist_ok=True)
    dataset_dir.mkdir(parents=True, exist_ok=True)
    collection_dir.mkdir(parents=True, exist_ok=True)
    technology_dir.mkdir(parents=True, exist_ok=True)
    dist_dir.mkdir(parents=True, exist_ok=True)

    for path in task_dir.glob("*.md"):
        path.unlink()
    for path in dataset_dir.glob("*.md"):
        path.unlink()
    for path in collection_dir.glob("*.md"):
        path.unlink()
    for path in technology_dir.glob("*.md"):
        path.unlink()

    populated_task_count = 0
    for task in tasks.values():
        matches = task_matches(task["id"], datasets)
        if task.get("status") != "active" or not matches:
            continue
        populated_task_count += 1
        (task_dir / f"{task['id']}.md").write_text(
            render_task_page(task, matches, labels, resources),
            encoding="utf-8",
        )

    for dataset in datasets.values():
        (dataset_dir / f"{dataset['id']}.md").write_text(
            render_dataset_page(dataset, tasks, labels, collections),
            encoding="utf-8",
        )

    for collection in collections.values():
        if collection.get("status") != "active":
            continue
        (collection_dir / f"{collection['id']}.md").write_text(
            render_collection_page(collection, datasets, resources, tasks),
            encoding="utf-8",
        )

    for technology_id, technology_name in labels.get("technologies", {}).items():
        matches = technology_matches(technology_id, datasets)
        if not matches:
            continue
        (technology_dir / f"{technology_id}.md").write_text(
            render_technology_page(
                technology_id, technology_name, matches, tasks, labels
            ),
            encoding="utf-8",
        )

    (root / "catalog" / "README.md").write_text(
        render_catalog_home(categories, tasks, datasets, collections, resources),
        encoding="utf-8",
    )

    (root / "catalog" / "datasets.md").write_text(
        render_dataset_index(datasets, tasks, labels),
        encoding="utf-8",
    )

    (root / "catalog" / "technologies.md").write_text(
        render_technology_index(datasets, labels),
        encoding="utf-8",
    )

    (root / "catalog" / "resources.md").write_text(
        render_resource_index(resources, collections),
        encoding="utf-8",
    )

    catalog = render_catalog_json(
        tasks, categories, datasets, vocabularies, collections, resources
    )
    (dist_dir / "catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    update_readme_stats(root, datasets, tasks, resources)
    update_readme_featured(root, datasets, tasks, labels)

    return {
        "tasks": populated_task_count,
        "datasets": len(datasets),
        "resources": len(resources),
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Wireless ML Data Hub catalogue artifacts.")
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root (defaults to current project root).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify generated files are current without modifying the repository.",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    if args.check:
        problems = check_generated(root)
        if problems:
            print("Generated catalogue is stale.")
            print()
            print(
                "Do not edit files under catalog/ or dist/catalog.json directly. "
                "Update the source data or generator, run scripts/build.py, and commit "
                "the regenerated artifacts."
            )
            print()
            print("Detected differences:")
            for problem in problems:
                print(f" - {problem}")
            return 1

        print("Generated catalogue is up to date.")
        return 0

    result = build(root)
    print(
        f"Generated catalogue: {result['datasets']} datasets, "
        f"{result['tasks']} populated task pages, "
        f"{result['resources']} supporting resources."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
