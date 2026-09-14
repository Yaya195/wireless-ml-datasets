# Contributing to Wireless ML Data Hub

Contributions are welcome. The goal is not to maximize the number of entries, but to maintain a useful, evidence-backed catalogue of datasets for machine learning in wireless communications.

## Ways to contribute

You can:

- suggest a dataset through the GitHub dataset-suggestion issue form;
- report incorrect or outdated metadata;
- propose a missing **wireless research task**;
- suggest a supporting benchmark, evaluation suite, or discovery portal;
- submit a pull request adding or correcting structured metadata.

A task in this project is a wireless research problem such as `beam-prediction`, `localization`, `radio-slam`, `radio-assisted-navigation`, or `spectrum-sensing`. It is not a generic ML formulation such as classification or regression.

## Development setup

The project uses `uv`.

```powershell
uv sync
```

You can run repository commands without manually activating the environment:

```powershell
uv run python scripts/validate.py
```

## Before adding a dataset

First search:

- `data/datasets/`;
- `catalog/datasets.md`;
- dataset aliases and official identifiers.

Then run:

```powershell
uv run python scripts/check_duplicates.py
```

The duplicate checker distinguishes strong identity collisions from review warnings. See [Curation Guidelines](docs/curation-guidelines.md) for the identity rules.

## Adding a dataset

Create one canonical YAML record under:

```text
data/datasets/<dataset-id>.yaml
```

Use a stable lowercase slug for the ID.

A new record should establish, where available:

- canonical dataset identity and version;
- official access path;
- release year and release notes;
- resource type: dataset, family, or collection;
- acquisition origin;
- modalities and wireless technology context;
- frequency/environment/mobility metadata;
- access and licensing;
- official resources and references;
- one or more evidence-backed Task↔Dataset mappings;
- caveats that materially affect reuse or comparison;
- metadata verification status and date.

Use an existing heterogeneous record as a starting point rather than inventing new field names.

## Dataset identity

Dataset identity is separate from publication identity.

```yaml
identity:
  canonical_url: https://example.org/dataset
  version: null
  external_ids:
    - scheme: doi
      value: 10.xxxx/example
```

Only put a DOI in `identity.external_ids` when the DOI identifies the dataset/resource itself. A paper DOI belongs in `references`.

Do not create a second record for a renamed version, subset, or derived resource without checking whether it should instead be represented using `relations`.

## Mapping datasets to wireless tasks

Every task mapping must be supported by evidence already listed in the record's `references`.

Do not add a task merely because the available variables make it seem possible.

When a task applies only to a subset or scenario within a larger collection, use task-specific `context` rather than inheriting broader collection-level metadata.

Use:

- `targets` for intrinsic outputs of the task;
- `evaluation_reference` for ground truth used to evaluate or geometrically interpret a result without redefining the task output.

For example, channel charting may use position as an evaluation reference without treating position as the channel-charting target.

### Verified task use vs. technical suitability

Keep demonstrated task membership separate from technical suitability. A dataset can contain the ingredients for a task without having been used for that task in an authoritative source.

In particular:

- geometry, delay, AoA/AoD, interaction points, or scene labels can make a dataset useful for Radio-SLAM research, but do not automatically justify a `radio-slam` mapping;
- sequential radio + position/IMU data can make a dataset useful for navigation research, but do not automatically justify `radio-assisted-navigation`;
- `radio-assisted-navigation` requires documented path/waypoint selection, motion guidance, navigation actions, or policy evaluation. Position or floor prediction alone remains `localization`;
- Radio-SLAM can be snapshot or sequential. Do not require a trajectory merely because many SLAM datasets are temporal.

The audit script may report informational spatial-suitability hints. These are leads for curator review, not evidence and not task mappings.

## Adding vocabulary values

Do not add a new controlled-vocabulary value just because an existing label feels imperfect.

Add one only when an actual dataset cannot be represented accurately with the existing vocabulary. Keep different semantic dimensions separate: technology, frequency regime, radio configuration, modality, and ground truth should not be mixed.

For technology metadata, preserve the abstraction level of the existing vocabulary:

- `6g` is a first-class technology/research-generation tag when an authoritative dataset, challenge, or project source explicitly positions the resource for 6G research. Do not infer `6g` merely from mmWave/sub-THz operation, massive MIMO, "next-generation" wording, or 6G-project funding.
- `lorawan` is a technology value; LoRa modulation/PHY is not a separate technology value in this vocabulary. Do not infer LoRaWAN from a LoRa waveform-only dataset.
- system/research paradigms such as ISAC are not technology values and must not be added to `technologies`.

## Adding or changing wireless tasks

Task definitions live under:

```text
data/tasks/
```

A task should represent a recognizable wireless research problem.

New tasks require evidence that the task is useful for organizing reusable datasets. A task can remain `candidate` until curated datasets support it.

Do not create a new task merely to accommodate one paper's terminology when an existing task already captures the research problem.


## Collections and supporting resources

Cross-cutting paradigms such as LLMs and foundation models belong under `data/collections/`; they are not wireless research tasks. Supporting benchmark datasets, evaluation suites/frameworks, competition platforms, and dataset portals belong under `data/resources/` when they help users benchmark models or continue a personalized search but should not inflate the core dataset count.

A supporting resource may link to an existing wireless task only when the relationship is explicitly evidenced. Do not use a collection or resource record to bypass the Dataset↔Task evidence rules.

## Contribution licensing

By submitting a contribution, you agree that your contribution may be distributed under the license that applies to the material you modify:

- software, schemas, tests, CI, and repository tooling are licensed under Apache-2.0;
- original catalogue metadata and project documentation are licensed under CC BY 4.0.

Do not copy third-party dataset contents, paper text, figures, or other material into this repository unless you have the rights to do so. Catalogue records should summarize and link to authoritative sources. The repository licenses do not alter the licenses or terms of the underlying datasets and external resources.

See [`LICENSE`](LICENSE) for the licensing map and full license texts.

## Generated files

Do **not** manually edit:

```text
catalog/README.md
catalog/datasets.md
catalog/resources.md
catalog/technologies.md
catalog/tasks/*.md
catalog/datasets/*.md
catalog/collections/*.md
catalog/technologies/*.md
dist/catalog.json
```

After changing source YAML, regenerate:

```powershell
uv run python scripts/build.py
```

Generated files are committed so the GitHub repository remains browsable without requiring Python.

## Required checks

Before opening a pull request, run:

```powershell
uv run python scripts/validate.py
uv run python scripts/check_duplicates.py
uv run python scripts/audit_task_coverage.py
uv run python scripts/audit_technology_coverage.py
uv run python scripts/build.py
uv run python scripts/build.py --check
uv run pytest
uv run ruff check scripts tests
```

All commands should pass.

`build.py --check` is non-mutating and verifies that committed generated files match the YAML source of truth.

## Pull-request expectations

A dataset PR should:

- explain why the resource belongs in the catalogue;
- link authoritative dataset/access sources;
- identify the wireless task(s) supported by evidence;
- avoid speculative metadata;
- distinguish unknown, not reported, and not applicable where the schema allows it;
- include generated catalogue updates;
- pass validation, duplicate checks, tests, formatting checks, and generated-file consistency checks.

Metadata status reflects confidence in the catalogue record, not scientific endorsement or dataset quality.
