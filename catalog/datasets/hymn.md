<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# HYMN: Hybrid Indoor and Indoor-Outdoor Positioning Multi-Technology Dataset

**Aliases:** HYbrid Multi-technology Navigation Dataset, HYMN Dataset

A synchronized multi-technology positioning dataset spanning indoor and indoor-outdoor conditions, with UWB, BLE, Wi-Fi, 5G NR, and GNSS observations aligned to reference coordinates for seamless localization and cross-technology fusion research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Range measurements, SNR / signal-quality measurements, GNSS observations, Position |
| Technologies | Wi-Fi, BLE, UWB, 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Indoor, Outdoor, Industrial |
| Mobility | Static |
| Temporal structure | Snapshot |
| Access | Open |
| License | CC BY 4.0 |

## Frequency

**Regimes:** Sub-6 GHz

Frequency depends on the positioning technology; the dataset combines Wi-Fi, BLE, UWB, 5G NR, and GNSS observations.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** Range measurements, SNR / signal-quality measurements, GNSS observations

**Targets:** Position

**Scope:** Seamless indoor and indoor-outdoor positioning and cross-technology localization/fusion using synchronized terrestrial radio and GNSS observations.

**Task context:** Environment: Indoor, Outdoor, Industrial · Mobility: Static · Frequency: Sub-6 GHz

Despite “Navigation” in the HYMN acronym, the documented benchmark scope is localization/positioning rather than route or action selection.

## Scale

- **Sites:** 1
- **Notes:** Measurements are synchronized across five positioning systems using common point identifiers; exact total sample count is technology-dependent.

## Resources

- [Dataset access](https://github.com/TUD-ITVS/HYMN-dataset)

## Caveats

- HYMN expands to “HYbrid Multi-technology Navigation”, but its published task evidence is localization and seamless positioning; do not infer a radio-assisted-navigation mapping from the name alone.

## References

- [HYMN dataset — official repository](https://github.com/TUD-ITVS/HYMN-dataset)
- [Descriptor: A Hybrid Indoor and Indoor–Outdoor Positioning Multitechnology Dataset (HYMN)](https://doi.org/10.1109/IEEEDATA.2026.3691044)
- [HYMN dataset release on Zenodo](https://doi.org/10.5281/zenodo.17979434)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
