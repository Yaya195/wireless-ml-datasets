<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# CSI-Bench

**Aliases:** CSI-Bench Real WiFi Sensing Benchmark

A large-scale in-the-wild Wi-Fi CSI benchmark spanning multiple sensing tasks, devices, users, and environments, with standardized splits for in-distribution and cross-device/environment/user evaluation.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Wi-Fi CSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Residential |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Registration required |
| License | CC BY-NC 4.0 |

## Frequency

**Status:** Varies

Individual recordings encode frequency in filenames; the benchmark spans multiple acquisition configurations.

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Activity label

**Scope:** Classify human activities from Wi-Fi CSI under in-distribution and cross-device/environment/user evaluation.

**Task context:** Environment: Indoor, Residential · Mobility: Not applicable

### [Vital Sign Sensing](../tasks/vital-sign-sensing.md)

**Inputs:** Wi-Fi CSI

**Targets:** Respiratory motion

**Scope:** Detect breathing-related states from Wi-Fi CSI using the benchmark's breathing-detection subset.

**Task context:** Environment: Indoor, Residential · Mobility: Not applicable

### [Localization](../tasks/localization.md)

**Inputs:** Wi-Fi CSI

**Targets:** Position

**Scope:** Estimate labeled indoor location from Wi-Fi CSI using the benchmark's localization subset.

**Task context:** Environment: Indoor, Residential · Mobility: Not applicable

## Scale

- **Notes:** The benchmark includes task-specific collections for fall detection, breathing, localization, motion-source recognition, human activity recognition, human identification, and proximity recognition.

## Resources

- [Dataset access](https://www.kaggle.com/datasets/guozhenjennzhu/csi-bench)
- [Official homepage](https://github.com/guozhen-jenn-zhu/CSI-Bench-Real-WiFi-Sensing-Benchmark)

## Caveats

- CSI-Bench has undergone post-publication data corrections; use the maintained current release (Kaggle Version 12 at verification time) rather than earlier copies.

## References

- [CSI-Bench Real WiFi Sensing Benchmark](https://github.com/guozhen-jenn-zhu/CSI-Bench-Real-WiFi-Sensing-Benchmark)
- [CSI-Bench: A Large-Scale In-the-Wild Dataset for Multi-Task WiFi Sensing](https://arxiv.org/abs/2505.21866)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
