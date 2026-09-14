<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RBS-ML Datasets for 5G Rogue Base Station Detection

Synthetic 5G vehicular received-signal-strength sequences containing legitimate and rogue base stations, released with ML-ready CSV files for rogue-base-station detection.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Simulation |
| Modalities | RSS, Mobility trace |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Outdoor, Vehicular |
| Mobility | Mobile |
| Temporal structure | Sequence |
| Access | Open |
| License | Academic/research use only |

## Frequency

**Regimes:** Sub-6 GHz

## Supported wireless tasks

### [Network Anomaly Detection](../tasks/network-anomaly-detection.md)

**Inputs:** RSS, Mobility trace

**Targets:** Anomaly label

**Scope:** Detect rogue 5G base stations from temporal received-signal-strength patterns in vehicular scenarios.

**Task context:** Environment: Vehicular, Outdoor · Mobility: Mobile · Frequency: Sub-6 GHz

## Resources

- [Dataset access](https://github.com/mohammadmsaedi/RBS-ML)

## Caveats

- The distributed ML data are synthetically generated from a vehicular radio simulation rather than captured from a live rogue-cell deployment.

## References

- [RBS-ML: datasets for 5G Rogue Base Station Detection](https://github.com/mohammadmsaedi/RBS-ML)
- [RBS-MLP Datasets for 5G Rogue Base Station Detection](https://openaccess.city.ac.uk/id/eprint/36127/)
- [Generation of realistic signal strength measurements for a 5G Rogue Base Station attack scenario](https://doi.org/10.1109/CNS48642.2020.9162275)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
