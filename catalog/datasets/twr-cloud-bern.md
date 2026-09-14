<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# TWR-CLOUD-Bern

**Aliases:** Two-Way-Ranging-based Cooperative Localization with an Open UWB Dataset from Bern-University

An open UWB two-way-ranging dataset for cooperative localization, collected with 40 Qorvo DWM3001C nodes over 12 scans at the University of Bern and distributed with official evaluation scenarios and scoring tools.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Range measurements, Position |
| Technologies | UWB |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Campus |
| Mobility | Unknown |
| Temporal structure | Unknown |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

The verified catalogue sources do not establish one collection-wide channel/frequency value.

## Supported wireless tasks

### [Cooperative Localization](../tasks/cooperative-localization.md)

**Inputs:** Range measurements

**Targets:** Position

**Scope:** Estimate node positions from inter-node UWB two-way-ranging measurements under anchor-free, anchor-aided, or anchor-only evaluation modes.

**Task context:** Environment: Indoor, Campus · Mobility: Unknown

## Scale

- **Scenarios:** 12
- **Devices:** 40
- **Sites:** 1
- **Size (GB):** 29.8
- **Notes:** Twelve scans cover more than 500 m²; eleven support model development and one is held out for evaluation.

## Resources

- [Dataset access](https://zenodo.org/records/20277908)
- [Official homepage](https://twr-cloud.inf.unibe.ch)

## Caveats

- The release includes several evaluation modes and an official held-out scan; results should state the selected scenario/mode rather than treating all scans as one interchangeable split.

## References

- [TWR-CLOUD-Bern, Version 5](https://zenodo.org/records/20277908)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
