<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Drive-Test-Based LTE Handover Dataset for Urban Bangladesh

**Aliases:** Drive-Test-Based LTE Handover Dataset for Cellular Mobility Studies in Urban Bangladesh

A real LTE drive-test dataset from Dhaka containing handover-labeled radio measurements, Layer-3 events, UE velocity, cell IDs, and GPS information in raw and ML-ready forms.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Network KPI, Mobility trace, Position |
| Technologies | LTE |
| Generation context | 4G |
| Radio configuration | — |
| Environment | Outdoor, Urban, Vehicular |
| Mobility | Mobile |
| Temporal structure | Trajectory |
| Access | Open |
| License | CC BY 4.0 |

## Frequency

**Status:** Not Reported

The Mendeley record focuses on handover/mobility measurements rather than a single reported carrier band.

## Supported wireless tasks

### [Handover Prediction](../tasks/handover-prediction.md)

**Inputs:** Network KPI, Mobility trace, Position

**Targets:** Handover event

**Scope:** Predict LTE handover events from time-varying radio quality, cell identity, velocity, GPS, and signaling information.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile

The processed data apply a 320 ms Time-to-Trigger logic to refine handover labeling for ML use.

## Scale

- **Sequences:** 3
- **Sites:** 1
- **Size (GB):** 0.024
- **Notes:** Three drive-test sessions cover a 13 km route; the distributed archive is approximately 24 MB.

## Resources

- [Dataset access](https://data.mendeley.com/datasets/n2pvmtyn2j)

## Caveats

- The measurements come from three sessions on one urban route and one regional LTE deployment; cross-operator and cross-city generalization should be evaluated separately.

## References

- [Drive-Test-Based LTE Handover Dataset for Cellular Mobility Studies in Urban Bangladesh](https://data.mendeley.com/datasets/n2pvmtyn2j)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
