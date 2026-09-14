<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Wi-Fi CSI and RSS Human Presence and Movement Dataset

**Aliases:** A Wi-Fi Channel State Information (CSI) and Received Signal Strength (RSS) data-set for human presence and movement detection

A 28 GB measured Wi-Fi dataset containing antenna-wise CSI and RSS traces with annotations for human presence and movement sensing.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI, RSS |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

A single catalogue-wide carrier/band was not verified from the Zenodo landing page.

## Supported wireless tasks

### [Presence Detection](../tasks/presence-detection.md)

**Inputs:** Wi-Fi CSI, RSS

**Targets:** Presence label

**Scope:** Detect human presence and movement state from annotated Wi-Fi CSI and/or RSS traces.

**Task context:** Environment: Indoor · Mobility: Not applicable

The release title and metadata explicitly identify human presence and movement detection as the sensing use.

## Scale

- **Size (GB):** 28.0
- **Notes:** Zenodo distributes paired compressed CSI JSON and RSS CSV files plus annotations.

## Resources

- [Dataset access](https://zenodo.org/records/3677366)

## Caveats

- The accompanying publication cited by the record uses RSS for movement detection; the Zenodo release also provides CSI, but experiments should state which representation is used.

## References

- [A Wi-Fi CSI and RSS data-set for human presence and movement detection](https://zenodo.org/records/3677366)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
