<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# ViWi

**Aliases:** ViWi Dataset

A vision-aided wireless dataset framework and scenario family combining rendered RGB/LiDAR context with ray-traced mmWave wireless data for beam and blockage research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset family |
| Origin | Ray tracing |
| Modalities | Channel matrix, Camera, LiDAR, Position, Scene geometry |
| Technologies | 6G |
| Generation context | 5G, 6G |
| Radio configuration | MIMO, Phased array |
| Environment | Outdoor, Urban, Vehicular |
| Mobility | Mobile |
| Temporal structure | Sequence |
| Access | Open |
| License | CC BY-NC-SA 4.0 |

## Frequency

**Regimes:** Sub-6 GHz, mmWave
**Bands:** 28 GHz

Core ViWi scenarios include 28 GHz mmWave links; some published ViWi applications combine visual data with sub-6 GHz channels.

## Supported wireless tasks

### [Beam Prediction](../tasks/beam-prediction.md)

**Inputs:** Camera

**Targets:** Beam index

**Scope:** ViWi applications use visual observations, optionally with wireless context, to predict mmWave beams.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: mmWave

### [Blockage Prediction](../tasks/blockage-prediction.md)

**Inputs:** Camera, Channel matrix

**Targets:** Blockage status

**Scope:** ViWi supports vision-aided future blockage prediction using image sequences and, in some formulations, sub-6 GHz channel information.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: Sub-6 GHz, mmWave

### [Beam Tracking](../tasks/beam-tracking.md)

**Inputs:** Camera

**Targets:** Beam index

**Scope:** The ViWi-BT dataset uses sequences of observed RGB images and beam indices to predict future mmWave beams.

**Task context:** Environment: Outdoor, Urban, Vehicular · Mobility: Mobile · Frequency: mmWave

Historical ViWi-BT development data were distributed as MAT, CSV, and H5 packages.

## Scale

- **Notes:** ViWi provides multiple scenario families and versioned generation packages rather than one fixed sample count.

## Resources

- [Dataset access](https://www.viwi-dataset.net/scenarios.html)
- [Official homepage](https://www.viwi-dataset.net/)

## Caveats

- ViWi is a scenario-generation framework/family rather than one immutable dataset; exact modalities and labels depend on the selected scenario, version, and generated configuration.

## References

- [ViWi: A Deep Learning Dataset Framework for Vision-Aided Wireless Communications](https://www.viwi-dataset.net/)
- [ViWi applications on vision-aided wireless communications](https://www.viwi-dataset.net/applications.html)
- [ViWi Vision-Aided Millimeter Wave Beam Tracking Competition](https://www.viwi-dataset.net/viwi-bt.html)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
