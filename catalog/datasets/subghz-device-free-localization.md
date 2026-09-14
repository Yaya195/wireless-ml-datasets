<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Sub-GHz Device-Free Localization Dataset

**Aliases:** Device-Free Localization & Identification Using Sub-GHz Passive Radio Mapping

A passive/device-free RSS dataset from 15 sub-GHz transceivers in a furnished office, with six human participants observed at 15 possible locations on 433 MHz and 868 MHz links.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | RSS, Position |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Office |
| Mobility | Not applicable |
| Temporal structure | Snapshot |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-GHz
**Bands:** 433 MHz, 868 MHz

Measurements use DASH7 links at 433 and 868 MHz.

## Supported wireless tasks

### [Device-Free Localization](../tasks/device-free-localization.md)

**Inputs:** RSS

**Targets:** Position

**Scope:** Estimate a stationary person's location from passive changes in sub-GHz RSS links without requiring a carried device.

**Task context:** Environment: Indoor, Office · Mobility: Not applicable · Frequency: Sub-GHz

## Scale

- **Participants:** 6
- **Devices:** 15
- **Size (GB):** 0.011
- **Notes:** Six people × 15 possible locations, measured over 15 transceiver links.

## Resources

- [Dataset access](https://zenodo.org/records/3941249)

## Caveats

- The dataset covers a single office and stationary participants at predefined locations; it is not a continuous tracking dataset.
- The source title uses “passive radio mapping” for fingerprint-based device-free localization; this does not establish a radio-map-estimation task.

## References

- [Device-Free Localization & Identification Using Sub-GHz Passive Radio Mapping](https://zenodo.org/records/3941249)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
