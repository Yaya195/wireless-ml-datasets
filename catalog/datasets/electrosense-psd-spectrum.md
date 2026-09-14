<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# ElectroSense PSD Spectrum Dataset

A crowdsensed PSD dataset built from six-hour full-spectrum sweeps at multiple ElectroSense sites, with labeled licensed-band spectrum portions for wireless technology/signal classification.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Spectrum |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Unknown |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-GHz, Sub-6 GHz
**Bands:** 24 MHz–1.7 GHz full sweep

Each sensor sweeps 24 MHz to 1.7 GHz; labeled licensed-band portions are distributed.

## Supported wireless tasks

### [Signal Classification](../tasks/signal-classification.md)

**Inputs:** Spectrum

**Targets:** Signal class

**Scope:** Classify licensed-band wireless technologies/signals from labeled PSD spectrum observations.

**Task context:** Environment: Unknown · Mobility: Static · Frequency: Sub-GHz, Sub-6 GHz

## Scale

- **Duration (hours):** 6.0
- **Size (GB):** 1.7
- **Notes:** Six hours of full-spectrum scan are collected per site; the distributed labeled archive is about 1.7 GB.

## Resources

- [Dataset access](https://zenodo.org/records/7521246)

## Caveats

- The release contains selected labeled licensed-band portions rather than uniformly labeled occupancy over every scanned frequency.

## References

- [ElectroSense PSD Spectrum Dataset](https://zenodo.org/records/7521246)
- [A Framework for Wireless Technology Classification using Crowdsensing Platforms](https://doi.org/10.1109/INFOCOM53939.2023.10228867)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
