<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# SHD-HAR

**Aliases:** Spatially-diverse High-dimensional CSI Dataset for Human Activity Recognition

A high-dimensional Wi-Fi CSI human-activity dataset collected synchronously from two diagonal ESP32 transceiver paths across ten macro- and micro-movements.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Laboratory |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 2.4 GHz Wi-Fi channel 11

IEEE 802.11n channel 11 with 20 MHz bandwidth is documented by the data article.

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Activity label

**Scope:** Recognize ten macro- and micro-movement activities from synchronized spatially diverse Wi-Fi CSI measurements.

**Task context:** Environment: Indoor, Laboratory · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Scenarios:** 1
- **Participants:** 6
- **Devices:** 4
- **Sites:** 1
- **Notes:** Ten activities were recorded from six participants with approximately 1,200 samples per activity and 300-450 packets per sample.

## Resources

- [Dataset access](https://zenodo.org/records/11201414)
- [Documentation](https://doi.org/10.1016/j.dib.2024.110673)

## References

- [Spatially-diverse High-dimensional Channel State Information (CSI) based Dataset for Human Activity Recognition (HAR)](https://zenodo.org/records/11201414)
- [A high-dimensional, multi-transceiver channel state information dataset for enhanced human activity recognition](https://doi.org/10.1016/j.dib.2024.110673)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-10-20`
