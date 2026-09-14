<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Position-Annotated BLE RSSI Dataset

BLE RSSI fingerprints and trajectories precisely annotated with AR/camera-based ground-truth positions, including stationary fingerprints, tracks, occupancy information, and precomputed radio-map grids.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | RSS, Position, Radio map |
| Technologies | BLE |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Office |
| Mobility | Mixed |
| Temporal structure | Trajectory |
| Access | Open |
| License | CC0 1.0 |

## Frequency

**Status:** Not Reported

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** RSS

**Targets:** Position

**Scope:** Evaluate BLE indoor localization and tracking using accurately position-annotated RSSI trajectories and fingerprints.

**Task context:** Environment: Indoor, Office · Mobility: Mixed

### [Radio Map Estimation](../tasks/radio-map-estimation.md)

**Inputs:** RSS, Position

**Targets:** Radio map

**Scope:** Estimate probabilistic BLE RSSI radio maps from sparsely sampled stationary fingerprints.

**Task context:** Environment: Indoor, Office · Mobility: Not applicable

The official repository distributes fingerprint histograms and grid radio-map products and points to neural-network radio-map estimation work.

## Resources

- [Dataset access](https://github.com/philotuxo/Position-Annotated-BLE-RSSI-Dataset)

## Caveats

- The release mixes stationary fingerprints, trajectories, occupancy maps, and precomputed radio-map grids; experiments should state which subset is used.

## References

- [Position Annotated BLE RSSI Dataset for Indoor Localization](https://github.com/philotuxo/Position-Annotated-BLE-RSSI-Dataset)
- [An indoor localization dataset and data collection framework with high precision position annotation](https://doi.org/10.1016/j.pmcj.2022.101554)
- [Radio map estimation with neural networks and active learning for indoor localization](https://ceur-ws.org/Vol-2498/short4.pdf)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
