# Machine-Readable Catalogue

`dist/catalog.json` is the generated machine-readable distribution of Wireless ML Data Hub.

It is built from the same YAML source used to generate the GitHub catalogue pages.

## Source of truth

The canonical source files are:

```text
data/datasets/*.yaml
data/tasks/*.yaml
data/collections/*.yaml
data/resources/*.yaml
data/task-categories.yaml
data/vocabularies.yaml
```

`dist/catalog.json` should not be edited manually.

## Top-level structure

The JSON document contains:

```json
{
  "schema_version": "...",
  "categories": [],
  "tasks": [],
  "datasets": [],
  "collections": [],
  "resources": [],
  "technology_index": [],
  "vocabularies": {}
}
```

### `categories`

Task-category definitions used to organize wireless research tasks.

### `tasks`

Only tasks currently populated by at least one curated dataset are distributed here.

### `datasets`

Canonical structured **core dataset** records, including their Task↔Dataset mappings and evidence. Supporting benchmark/platform records do not inflate this array or its count.

### `collections`

Cross-cutting thematic groupings such as LLM and foundation-model resources. Collections are an organizational axis and are not wireless research tasks.

### `resources`

Curated supporting benchmark datasets, evaluation suites/frameworks, competition platforms, dataset collections, and discovery portals. A resource may link to a wireless task when that relationship is explicitly evidenced, but it is not counted as a core Dataset↔Task mapping.

### `technology_index`

A generated secondary discovery index with each technology ID, display name, core-dataset count, and matching dataset IDs. Task remains the primary organization; this index supports filtering and technology-oriented browsing such as 6G.

### `vocabularies`

Machine IDs and human-readable labels for controlled metadata fields.

## Stability

Stable dataset and task IDs are intended for downstream references.

Human-readable labels, descriptions, verification notes, and metadata may evolve as sources are rechecked.

The `schema_version` field changes when the generated JSON structure changes in a way that downstream consumers may need to account for.

## Regeneration

```powershell
uv run python scripts/build.py
```

To verify that committed generated files are current without modifying them:

```powershell
uv run python scripts/build.py --check
```

The generated JSON is intended to support future search interfaces, filtering, websites, and grounded assistants without requiring Markdown parsing.
