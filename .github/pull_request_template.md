## Summary

Describe the dataset, metadata correction, task change, or infrastructure change.

## Evidence

For dataset/task changes, link the authoritative sources supporting the metadata and Task↔Dataset mapping.

## Checklist

- [ ] I checked for an existing dataset record, alias, version, or related collection.
- [ ] Dataset identity is separate from paper identity.
- [ ] Every Task↔Dataset mapping is evidence-backed.
- [ ] I did not manually edit generated catalogue files.
- [ ] I regenerated the catalogue with `uv run python scripts/build.py`.
- [ ] `uv run python scripts/validate.py` passes.
- [ ] `uv run python scripts/check_duplicates.py` passes without unresolved duplicate errors.
- [ ] `uv run python scripts/build.py --check` passes.
- [ ] `uv run pytest` passes.
- [ ] `uv run ruff check scripts tests` passes.
