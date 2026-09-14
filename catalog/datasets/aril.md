<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# ARIL

Wi-Fi CSI fingerprints collected with Ettus N210 hardware for the joint tasks of six-class human activity recognition and 16-location indoor localization.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | SISO |
| Environment | Indoor |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Activity label

**Scope:** Recognize one of six human activities from Wi-Fi CSI fingerprints.

**Task context:** Environment: Indoor · Mobility: Not applicable

### [Localization](../tasks/localization.md)

**Inputs:** Wi-Fi CSI

**Targets:** Position

**Scope:** Classify the indoor location associated with Wi-Fi CSI fingerprints.

**Task context:** Environment: Indoor · Mobility: Static

## Scale

- **Samples:** 1,394
- **Scenarios:** 16
- **Notes:** The paper reports more than 1,400 CSI fingerprints, six activities and 16 locations.

## Resources

- [Dataset access](https://github.com/geekfeiw/ARIL)

## References

- [ARIL: Joint Activity Recognition and Indoor Localization with WiFi Fingerprints](https://github.com/geekfeiw/ARIL)
- [Joint Activity Recognition and Indoor Localization With WiFi Fingerprints](https://doi.org/10.1109/ACCESS.2019.2923743)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
