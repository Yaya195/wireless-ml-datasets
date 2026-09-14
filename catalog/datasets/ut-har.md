<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# UT-HAR

A widely used Intel 5300 Wi-Fi CSI human-activity-recognition dataset with seven activity classes and approximately five thousand segmented benchmark samples.

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

**Status:** Not Reported

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Activity label

**Scope:** Classify seven indoor human activities from Wi-Fi CSI amplitude/phase sequences.

**Task context:** Environment: Indoor · Mobility: Not applicable

## Scale

- **Samples:** 4,973
- **Notes:** SenseFi reports 3,977 training and 996 testing samples after benchmark preprocessing.

## Resources

- [Dataset access](https://github.com/ermongroup/Wifi_Activity_Recognition)

## Caveats

- The original continuous data do not provide ideal activity segmentation; common benchmark versions use windowing/segmentation that can introduce repeated content.

## References

- [Wifi Activity Recognition / UT-HAR](https://github.com/ermongroup/Wifi_Activity_Recognition)
- [SenseFi: A library and benchmark on deep-learning-empowered WiFi human sensing](https://doi.org/10.1016/j.patter.2023.100703)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
