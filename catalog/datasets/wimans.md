<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# WiMANS

**Aliases:** WiMANS Multi-User Activity Sensing Dataset

A multi-user Wi-Fi CSI sensing dataset with 11,286 synchronized three-second samples across 2.4/5 GHz, zero to five concurrent users, and identity, location, and activity annotations.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 2.4 GHz Wi-Fi, 5 GHz Wi-Fi

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Activity label

**Scope:** Recognize concurrent human activities from dual-band Wi-Fi CSI in multi-user indoor scenes.

**Task context:** Environment: Indoor · Mobility: Not applicable · Frequency: Sub-6 GHz

The official benchmark evaluates activity, identity, and location recognition; location is represented separately as a device-free localization mapping.

### [Device-Free Localization](../tasks/device-free-localization.md)

**Inputs:** Wi-Fi CSI

**Targets:** Position

**Scope:** Recognize the discrete indoor location of one or more people from dual-band Wi-Fi CSI without requiring them to carry a radio device.

**Task context:** Environment: Indoor · Mobility: Not applicable · Frequency: Sub-6 GHz

WiMANS benchmarks a location task over five labeled locations (A–E) per environment; the target is categorical location rather than continuous metric coordinates.

## Scale

- **Samples:** 11,286
- **Participants:** 5
- **Notes:** Each three-second sample contains 0–5 simultaneous users with identity, location, and activity annotations.

## Resources

- [Dataset access](https://www.kaggle.com/datasets/shuokanghuang/wimans)
- [Official homepage](https://github.com/huangshk/WiMANS)

## Caveats

- Samples may contain multiple users performing different activities simultaneously, so evaluation assumptions differ from single-person HAR datasets.

## References

- [WiMANS](https://github.com/huangshk/WiMANS)
- [WiMANS: A Benchmark Dataset for WiFi-Based Multi-User Activity Sensing](https://doi.org/10.1007/978-3-031-72946-1_5)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
