<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# MM-Fi

**Aliases:** MMFi

A multimodal non-intrusive human-sensing dataset with more than 320,000 synchronized frames from 40 participants in four environments, including Wi-Fi CSI, mmWave, LiDAR, depth/infrared, and pose/action annotations.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI, Radar, LiDAR, Camera, Position |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Varies

Wireless modalities use distinct Wi-Fi/mmWave configurations; no single catalogue-wide band is assigned.

## Supported wireless tasks

### [Pose Estimation](../tasks/pose-estimation.md)

**Inputs:** Wi-Fi CSI, Radar

**Targets:** Pose / keypoints

**Scope:** Estimate 2D/3D human pose from wireless sensing modalities such as Wi-Fi CSI and mmWave.

**Task context:** Environment: Indoor · Mobility: Not applicable

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI, Radar

**Targets:** Activity label

**Scope:** Recognize 27 daily and rehabilitation activities from wireless sensing modalities.

**Task context:** Environment: Indoor · Mobility: Not applicable

## Scale

- **Samples:** 320,000
- **Scenarios:** 4
- **Participants:** 40
- **Notes:** The dataset contains over 320k synchronized frames, 40 subjects, four environmental domains, and 27 actions.

## Resources

- [Dataset access](https://ntu-aiot-lab.github.io/mm-fi)
- [Official repository](https://github.com/ybhbingo/MMFi_dataset)

## Caveats

- MM-Fi is multimodal and some raw visual modalities are restricted for privacy; wireless-only experiments should explicitly state which public modalities are used.

## References

- [Toolbox for MM-Fi Dataset](https://github.com/ybhbingo/MMFi_dataset)
- [MM-Fi: Multi-Modal Non-Intrusive 4D Human Dataset for Versatile Wireless Sensing](https://openreview.net/forum?id=1uAsASS1th)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
