<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# mmHSense

**Aliases:** Multi-Modal and Distributed mmWave ISAC Datasets for Human Sensing

A collection of six open labeled mmWave ISAC datasets spanning gesture recognition, skeletal pose estimation, localization, and gait/person identification with CSI, beam-SNR, and related mmWave sensing features.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Channel matrix, Beam power |
| Technologies | Wi-Fi, 5G NR |
| Generation context | 5G |
| Radio configuration | Phased array |
| Environment | Indoor, Laboratory |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Registration required |
| License | CC BY 4.0 |

## Frequency

**Regimes:** mmWave
**Bands:** 60 GHz (Wi-Fi subsets)

The collection includes 60 GHz Wi-Fi sensing and a separate 5G mmWave gesture subset; exact settings vary by sub-dataset.

## Supported wireless tasks

### [Gesture Recognition](../tasks/gesture-recognition.md)

**Inputs:** Channel matrix, Beam power

**Targets:** Gesture label

**Scope:** Recognize human gestures from mmWave Wi-Fi or 5G sensing features.

**Task context:** Environment: Indoor, Laboratory · Mobility: Not applicable · Frequency: mmWave

The collection includes both mmWGesture and 5GmmGesture.

### [Pose Estimation](../tasks/pose-estimation.md)

**Inputs:** Channel matrix

**Targets:** Pose / keypoints

**Scope:** Estimate skeletal human pose from mmWave CSI/sensing features.

**Task context:** Environment: Indoor, Laboratory · Mobility: Not applicable · Frequency: mmWave

Supported by mmWPose and DISAC-mmVRPose.

### [Localization](../tasks/localization.md)

**Inputs:** Beam power

**Targets:** Position

**Scope:** Estimate discrete human/location states using the mmW-Loc sensing subset.

**Task context:** Environment: Indoor, Laboratory · Mobility: Not applicable · Frequency: mmWave

The mmW-Loc release supports localization with optional background subtraction.

## Scale

- **Scenarios:** 6
- **Notes:** The collection comprises mmWGesture, 5GmmGesture, mmWPose, DISAC-mmVRPose, mmW-Loc, and mmW-GaitID.

## Resources

- [Dataset access](https://ieee-dataport.org/documents/mmwavexr-multi-modal-and-distributed-mmwave-isac-datasets-human-sensing)
- [Official homepage](https://github.com/nisarnabeel/Multi-Modal-and-Distributed-mmWave-ISAC-Datasets-for-Human-Sensing)

## Caveats

- mmHSense is a heterogeneous collection: signal feature, hardware, geometry, labels, subjects, and sampling configuration differ by sub-dataset.

## References

- [mmHSense official code and dataset guide](https://github.com/nisarnabeel/Multi-Modal-and-Distributed-mmWave-ISAC-Datasets-for-Human-Sensing)
- [mmWavexR: Multi-Modal and Distributed mmWave ISAC Datasets for Human Sensing](https://ieee-dataport.org/documents/mmwavexr-multi-modal-and-distributed-mmwave-isac-datasets-human-sensing)
- [mmHSense: Multi-Modal and Distributed mmWave ISAC Datasets for Human Sensing](https://doi.org/10.1109/ACCESS.2026.3691174)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
