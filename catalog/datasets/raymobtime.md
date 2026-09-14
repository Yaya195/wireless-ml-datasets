<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Raymobtime

**Aliases:** RayMobTime

A collection of time-consistent ray-tracing datasets with mobility, channel data, and optional RGB/LiDAR modalities for beam management, blockage, channel prediction, and localization research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Ray tracing |
| Modalities | Channel matrix, Path parameters, Camera, LiDAR, Position, Mobility trace |
| Technologies | 6G |
| Generation context | 5G, 6G |
| Radio configuration | MIMO |
| Environment | Indoor, Outdoor, Urban, Vehicular |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz, mmWave
**Bands:** 2.8 GHz, 5 GHz, 28 GHz, 60 GHz

Frequency is scenario-dependent; the public scenario catalogue includes sub-6 GHz and mmWave configurations.

## Supported wireless tasks

### [Beam Selection](../tasks/beam-selection.md)

**Inputs:** Channel matrix

**Targets:** Beam index

**Scope:** Multiple Raymobtime scenarios are explicitly released for ML-based beam selection.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mixed · Frequency: Sub-6 GHz, mmWave

### [Beam Prediction](../tasks/beam-prediction.md)

**Inputs:** Camera

**Targets:** Beam index

**Scope:** The project explicitly lists beam prediction as a core use case, including multimodal scenarios.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: mmWave

Available input modalities are scenario-dependent; multimodal releases add camera and LiDAR alongside radio data.

### [Beam Tracking](../tasks/beam-tracking.md)

**Inputs:** Channel matrix

**Targets:** Beam index

**Scope:** Dedicated sequential mmWave V2I scenarios are released for beam tracking.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: mmWave

### [Blockage Prediction](../tasks/blockage-prediction.md)

**Inputs:** Camera, LiDAR

**Targets:** Blockage status

**Scope:** Raymobtime explicitly lists future blockage prediction as a supported use case for dynamic multimodal scenarios.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: mmWave

### [Channel Prediction](../tasks/channel-prediction.md)

**Inputs:** Channel matrix

**Targets:** Channel

**Scope:** Time-consistent channel sequences are provided for prediction of future channel state.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: Sub-6 GHz, mmWave

### [Localization](../tasks/localization.md)

**Inputs:** Channel matrix

**Targets:** Position

**Scope:** The project lists UE localization and position prediction among its core use cases and provides aligned channel/position data.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: Sub-6 GHz, mmWave

### [Mobility Prediction](../tasks/mobility-prediction.md)

**Inputs:** Position, Mobility trace

**Targets:** Position

**Scope:** Predict future UE positions from temporally consistent mobility and position sequences.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: Sub-6 GHz, mmWave

The official project lists UE localization and position prediction as a core use case.

## Scale

- **Scenarios:** 21
- **Notes:** The current public scenario catalogue enumerates 21 numbered scenarios with different frequencies, mobility patterns, and modalities.

## Resources

- [Dataset access](https://raymobtime.lasseufpa.org/scenarios/)
- [Official homepage](https://raymobtime.lasseufpa.org/)

## Caveats

- Raymobtime is a heterogeneous scenario collection; not every scenario contains every modality or supports every listed task, so task-specific scenario selection is essential.

## References

- [Raymobtime](https://raymobtime.lasseufpa.org/)
- [Raymobtime datasets and scenarios](https://raymobtime.lasseufpa.org/scenarios/)
- [Raymobtime publications by scenario and application](https://raymobtime.lasseufpa.org/publications/)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
