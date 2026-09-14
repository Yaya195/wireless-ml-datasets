<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# UAVSig

**Aliases:** UAV Signal Dataset

A measured RF dataset of drones and remote controllers collected for RF fingerprinting and device identification, distributed with raw captures, labels, metadata, and download tooling.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Outdoor, Laboratory |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | CC0 1.0 |

## Frequency

**Regimes:** Sub-6 GHz

Capture parameters vary by device/session; see dataset documentation.

## Supported wireless tasks

### [RF Fingerprinting](../tasks/rf-fingerprinting.md)

**Inputs:** I/Q samples

**Targets:** Device ID

**Scope:** Identify individual drones and remote controllers from their measured RF fingerprints.

**Task context:** Environment: Outdoor, Laboratory · Mobility: Mixed · Frequency: Sub-6 GHz

## Scale

- **Notes:** The Dataverse release contains hundreds of capture files plus metadata and helper scripts.

## Resources

- [Dataset access](https://dataverse.ucla.edu/dataset.xhtml?persistentId=doi:10.25346/S6/LVRRAE)
- [Official homepage](https://cores.ee.ucla.edu/downloads/datasets/uavsig/)

## Caveats

- The authors report random gaps in some raw-IQ capture segments caused by receiver sample drops; labels remain aligned to the received signals.

## References

- [UAVSig: Drone RF Signal Detection and Fingerprinting Dataset](https://dataverse.ucla.edu/dataset.xhtml?persistentId=doi:10.25346/S6/LVRRAE)
- [UAVSig](https://cores.ee.ucla.edu/downloads/datasets/uavsig/)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
