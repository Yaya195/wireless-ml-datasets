<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# ARLCL

**Aliases:** Anchor-free Ranging-Likelihood-based Cooperative Localization Dataset

A BLE RSS cooperative-localization dataset containing tens of thousands of evaluation scenarios with node ground truth and repeated resampling cases for anchor-free ranging-likelihood localization.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | RSS, Position |
| Technologies | BLE |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Campus |
| Mobility | Static |
| Temporal structure | Snapshot |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz

## Supported wireless tasks

### [Cooperative Localization](../tasks/cooperative-localization.md)

**Inputs:** RSS

**Targets:** Position

**Scope:** Estimate relative/absolute node positions cooperatively from inter-node BLE RSS measurements.

**Task context:** Environment: Indoor, Campus · Mobility: Static · Frequency: Sub-6 GHz

## Scale

- **Samples:** 68,440
- **Devices:** 21
- **Size (GB):** 5.9
- **Notes:** 68,440 compressed evaluation files/scenarios; maximum setting uses 21 Raspberry Pis.

## Resources

- [Dataset access](https://zenodo.org/records/7552462)
- [Official repository](https://github.com/CDS-Bern/ARLCL-Optimizer)

## Caveats

- The database-file structure is tightly coupled to the accompanying cooperative-localization optimizer/evaluation workflow.

## References

- [ARLCL: Anchor-free Ranging-Likelihood-based Cooperative Localization](https://zenodo.org/records/7552462)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
