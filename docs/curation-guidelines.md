# Curation Guidelines

These rules apply when adding or updating dataset records.

## 1. Establish dataset identity first

Before creating a new YAML record, determine whether the resource is actually new.

Each dataset record has an `identity` block:

```yaml
identity:
  canonical_url: https://example.org/dataset
  version: null
  external_ids:
    - scheme: doi
      value: 10.xxxx/example
```

### Canonical URL

Use `canonical_url` only when the URL identifies that dataset or collection specifically.

Do not use a generic host page shared by several datasets as the canonical identity URL.
A generic page may still be recorded under `access`, `official_resources`, or `references`.

### External identifiers

Only put identifiers in `identity.external_ids` when they identify the dataset/resource itself.

A DOI for a paper that describes or uses a dataset belongs in `references`, not in
`identity.external_ids`.

## 2. Duplicate-check policy

Run:

```powershell
uv run python scripts/check_duplicates.py
```

The checker distinguishes:

- **ERROR**: explicit identity collision, such as the same canonical dataset URL or the same external dataset identifier.
- **WARNING**: probable duplicate requiring review, such as overlapping names/aliases, authoritative URLs, or publication DOIs.

Warnings do not fail the normal command because some overlaps are legitimate.

For a stricter manual audit:

```powershell
uv run python scripts/check_duplicates.py --strict-warnings
```

## 3. Versions, subsets, and derived resources

Do not merge genuinely distinct resources just because their names are similar.

When separate records are justified, declare their relationship where applicable:

```yaml
relations:
  parent: parent-dataset-id
  supersedes:
    - older-dataset-id
  derived_from:
    - source-dataset-id
```

Relationship targets must already exist in the catalogue.

## 4. Task-specific context

Dataset-level metadata describes the resource as a whole.

If evidence for a wireless task applies only to a subset, scenario, or setup, put the
narrower metadata in the task mapping:

```yaml
tasks:
  - task: beam-prediction
    inputs:
      - position
    targets:
      - beam-index
    context:
      environments:
        - outdoor
      mobility: mobile
      frequency_regimes:
        - mmwave
```

Do not inherit broad collection-level metadata when the evidence is narrower.

## 5. Evidence discipline

Every Dataset↔Task mapping must cite evidence already present in the record's `references`.

Do not add a task merely because it seems technically possible with the data. The catalogue
records demonstrated or explicitly supported uses, not speculative ones.


## 6. Prediction targets versus evaluation references

Do not force every wireless task into a supervised input→target formulation.

Use `targets` only for variables that are intrinsic outputs of the task. The list may be empty.

Use `evaluation_reference` when ground truth is used to evaluate, align, or geometrically
interpret a result but is not itself the task output.

Example for channel charting:

```yaml
tasks:
  - task: channel-charting
    inputs:
      - channel-matrix
    targets: []
    evaluation_reference:
      - position
```

Position labels can be used to evaluate whether a learned channel chart preserves physical
geometry without redefining channel charting as position regression.


## 7. Cross-cutting collections are not wireless tasks

Use `data/collections/` for paradigms or themes such as LLM and foundation-model resources that cut across wireless problems. A collection organizes discovery; it does not create a new Dataset↔Task mapping.

## 8. Supporting benchmark and discovery resources

Use `data/resources/` for established benchmark suites/frameworks, competition platforms, dataset collections, and data portals that help users benchmark models or continue a personalized search. These records are deliberately excluded from the core dataset count.

A resource may include `task_links` only when an authoritative source explicitly supports the relationship. General portals normally have no task links.
## 9. Technology tags and 6G

Wireless task remains the primary discovery axis, while `technologies` is a secondary filter/browse dimension.

Use `6g` when an authoritative source for the dataset, challenge, or project explicitly positions the resource for 6G research. Research-stage status is not a reason to exclude a 6G dataset from this technology axis. Conversely, do not infer `6g` from mmWave/sub-THz frequencies, massive MIMO, generic "next-generation" language, or funding context alone.

Keep abstraction levels separate. `lorawan` may appear under `technologies`; LoRa PHY/modulation must not be introduced as a peer technology value. Likewise, system/research paradigms such as ISAC are outside the technology vocabulary.

