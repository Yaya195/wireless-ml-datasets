<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Wi-Pose

**Aliases:** Wi-Pose Dataset

A public 5 GHz Wi-Fi CSI human-pose dataset with 166,600 packets, 18-keypoint pose annotations, 12 actions, and 12 volunteers.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | MIMO |
| Environment | Indoor |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 5 GHz Wi-Fi

## Supported wireless tasks

### [Pose Estimation](../tasks/pose-estimation.md)

**Inputs:** Wi-Fi CSI

**Targets:** Pose / keypoints

**Scope:** Estimate 18-point human body pose from 5 GHz Wi-Fi CSI.

**Task context:** Environment: Indoor · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Samples:** 166,600
- **Participants:** 12
- **Notes:** Twelve volunteers perform 12 actions; pose annotations contain 18 skeleton points.

## Resources

- [Dataset access](https://github.com/NjtechCVLab/Wi-PoseDataset)

## Caveats

- Public Wi-Pose omits participant images for privacy; the released pose labels are camera-derived skeleton annotations.

## References

- [Wi-Pose Dataset](https://github.com/NjtechCVLab/Wi-PoseDataset)
- [CSI-Former: Pay More Attention to Pose Estimation with WiFi](https://doi.org/10.3390/e25010020)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
