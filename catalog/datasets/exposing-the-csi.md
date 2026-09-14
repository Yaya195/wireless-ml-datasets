<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Exposing the CSI

**Aliases:** Exposing the CSI Dataset

A measured 802.11ax CSI activity-recognition dataset with 12 activities, seven scenarios, three participants/environments, three synchronized Wi-Fi receivers, and anonymized video-derived reference keypoints.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Wi-Fi CSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | MIMO |
| Environment | Indoor, Laboratory, Office |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Varies |

## Frequency

**Status:** Not Reported

The verified project page states 160 MHz 802.11ax acquisition but no single catalogue-wide center frequency.

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Activity label

**Scope:** Recognize 12 indoor human activities from multi-receiver 802.11ax CSI sequences.

**Task context:** Environment: Indoor, Laboratory, Office · Mobility: Not applicable

Reference video keypoints are provided as auxiliary ground truth, but this catalogue mapping does not relabel the dataset as a wireless pose-estimation benchmark.

## Scale

- **Scenarios:** 7
- **Participants:** 3
- **Duration (hours):** 1.87
- **Size (GB):** 77.0
- **Notes:** Each scenario contains 12 activities recorded for 80 seconds; scenario archives are approximately 11 GB each.

## Resources

- [Dataset access](https://github.com/ansresearch/exposing-the-csi)

## Caveats

- Seven scenarios differ by participant, environment, and collection day; cross-scenario evaluation should preserve those domain-shift distinctions.

## References

- [Exposing the CSI dataset and resources](https://github.com/ansresearch/exposing-the-csi)
- [Exposing the CSI: A Systematic Investigation of CSI-based Wi-Fi Sensing Capabilities and Limitations](https://doi.org/10.1109/PERCOM56429.2023.10099368)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
