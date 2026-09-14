<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# UTHAMO

**Aliases:** UTHAMO: A Multi-Modal Wi-Fi CSI-Based Hand Motion Dataset

A multimodal hand-motion dataset providing Wi-Fi CSI, video trajectories, and IMU measurements for four gestures performed by six participants under multiple body orientations.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI, IMU, Camera |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | MIMO |
| Environment | Indoor, Office |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 2.4 GHz Wi-Fi

Published experiments use a 2.4 GHz Raspberry Pi transmitter and multi-antenna Wi-Fi receiver.

## Supported wireless tasks

### [Gesture Recognition](../tasks/gesture-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Gesture label

**Scope:** Recognize four hand gestures from commodity Wi-Fi CSI under participant and orientation variation.

**Task context:** Environment: Indoor, Office · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Participants:** 6
- **Notes:** Four hand gestures with repeated trials and multiple body orientations.

## Resources

- [Dataset access](https://doi.org/10.21227/QJFG-S580)
- [Official homepage](https://dorf.navidhasanzadeh.com/)

## Caveats

- The release is multimodal, but the catalogue task mapping records the explicitly demonstrated Wi-Fi CSI gesture-recognition use.

## References

- [DoRF / UTHAMO Project](https://dorf.navidhasanzadeh.com/)
- [UTHAMO: A Multi-Modal Wi-Fi CSI-Based Hand Motion Dataset](https://doi.org/10.21227/QJFG-S580)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
