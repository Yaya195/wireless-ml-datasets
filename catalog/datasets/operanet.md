<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# OPERAnet

**Aliases:** OPERAnet Multimodal Activity Recognition Dataset

A synchronized multimodal passive-sensing dataset with Wi-Fi CSI, UWB, passive Wi-Fi radar, and vision/infrared measurements from six participants performing six activities across two indoor rooms.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI, Channel impulse response, Position |
| Technologies | Wi-Fi, UWB |
| Generation context | — |
| Radio configuration | MIMO |
| Environment | Indoor |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz

Wi-Fi and UWB sensing modalities use different radio configurations.

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI, Channel impulse response

**Targets:** Activity label

**Scope:** Recognize six indoor human activities from Wi-Fi CSI and/or UWB channel measurements.

**Task context:** Environment: Indoor · Mobility: Not applicable · Frequency: Sub-6 GHz

The synchronized collection also contains dedicated CSI localization experiments, represented separately below.

### [Device-Free Localization](../tasks/device-free-localization.md)

**Inputs:** Wi-Fi CSI

**Targets:** Position

**Scope:** Localize a passive human target from dedicated Wi-Fi CSI experiments with static positions and short walking trajectories.

**Task context:** Environment: Indoor · Mobility: Mixed · Frequency: Sub-6 GHz

Experiments exp035–exp048 are explicitly described as device-free static/dynamic target-localization experiments with UWB-tag ground truth.

### [Localization](../tasks/localization.md)

**Inputs:** Wi-Fi CSI

**Targets:** Position

**Scope:** Device-to-device CSI localization using dedicated transmitter/receiver placement experiments with ground-truth coordinates.

**Task context:** Environment: Indoor · Mobility: Static · Frequency: Sub-6 GHz

Experiments exp049–exp054 are explicitly documented as device-to-device localization experiments.

## Scale

- **Scenarios:** 2
- **Participants:** 6
- **Duration (hours):** 8.0
- **Notes:** Approximately eight hours of annotated measurements across two rooms and six activities.

## Resources

- [Dataset access](https://springernature.figshare.com/collections/A_Comprehensive_Multimodal_Activity_Recognition_Dataset_Acquired_from_Radio_Frequency_and_Vision-Based_Sensors/5551209)
- [Documentation](https://doi.org/10.1038/s41597-022-01573-2)

## Caveats

- The six-participant/two-room collection is multimodal; wireless-only studies should state which RF modality is used.

## References

- [A Comprehensive Multimodal Activity Recognition Dataset Acquired from Radio Frequency and Vision-Based Sensors](https://springernature.figshare.com/collections/A_Comprehensive_Multimodal_Activity_Recognition_Dataset_Acquired_from_Radio_Frequency_and_Vision-Based_Sensors/5551209)
- [OPERAnet, a multimodal activity recognition dataset acquired from radio frequency and vision-based sensors](https://doi.org/10.1038/s41597-022-01573-2)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
