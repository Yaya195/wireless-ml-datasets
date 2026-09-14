<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# SignFi

A Wi-Fi CSI dataset collection for sign-language and gesture recognition, with segmented CSI traces and gesture labels from laboratory and home environments.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Wi-Fi CSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Laboratory, Residential |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | SignFi Dataset Terms of Use |

## Frequency

**Status:** Not Reported

The official dataset page identifies 802.11n CSI acquisition but does not state a single collection-wide carrier frequency.

## Supported wireless tasks

### [Gesture Recognition](../tasks/gesture-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Gesture label

**Scope:** Recognize sign-language gestures from segmented Wi-Fi CSI sequences.

**Task context:** Environment: Indoor, Laboratory, Residential · Mobility: Not applicable

## Scale

- **Notes:** The release includes 276-sign one-user lab/home subsets and a 150-sign lab subset with five users; counts differ by file and uplink/downlink variant.

## Resources

- [Dataset access](https://yongsen.github.io/SignFi/)
- [Official repository](https://github.com/yongsen/SignFi)

## Caveats

- SignFi's custom terms restrict the dataset to non-commercial educational/research use and prohibit redistribution without prior approval; downstream users should review the full terms before use.

## References

- [SignFi: Sign Language Recognition using WiFi and Convolutional Neural Networks](https://yongsen.github.io/SignFi/)
- [SignFi: Sign Language Recognition Using WiFi](https://doi.org/10.1145/3191755)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
