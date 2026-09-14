<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# UWB Non-Cooperative Contextual Sensing Dataset

**Aliases:** A Comprehensive Ultra-Wideband (UWB) Dataset for Non-Cooperative Contextual Sensing

A measured residential UWB CIR dataset for passive/device-free localization and human activity recognition, with background/no-target data, activity labels, and ground-truth target coordinates.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Channel impulse response, Position |
| Technologies | UWB |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Residential |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

The catalogue does not assign a single band without carrying over hardware-specific configuration details from the descriptor.

## Supported wireless tasks

### [Device-Free Localization](../tasks/device-free-localization.md)

**Inputs:** Channel impulse response

**Targets:** Position

**Scope:** Passively estimate the position of a human target from multistatic UWB CIR measurements.

**Task context:** Environment: Indoor, Residential · Mobility: Not applicable

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Channel impulse response

**Targets:** Activity label

**Scope:** Recognize walking, sitting, standing, and no-activity states from UWB CIR sequences.

**Task context:** Environment: Indoor, Residential · Mobility: Not applicable

### [Presence Detection](../tasks/presence-detection.md)

**Inputs:** Channel impulse response

**Targets:** Presence label

**Scope:** Distinguish target-present conditions from empty-room/background measurements using changes in the UWB CIR.

**Task context:** Environment: Indoor, Residential · Mobility: Not applicable

Presence is encoded by the separate background/no-target and target-present recordings; the descriptor explicitly discusses using their CIR difference to detect an immobile target.

## Scale

- **Samples:** 3,000,000
- **Participants:** 1
- **Sites:** 1
- **Duration (hours):** 1.6
- **Notes:** Approximately three million annotated points across walking, sitting, standing, no-activity, and empty-room/background periods.

## Resources

- [Dataset access](https://figshare.com/collections/A_Comprehensive_Ultra-Wideband_UWB_Dataset_for_Non-Cooperative_Contextual_Sensing/6078021)
- [Documentation](https://doi.org/10.1038/s41597-022-01776-7)

## Caveats

- The study contains one participant in one residence; activity and passive-localization results should not be interpreted as broad cross-person or cross-home generalization.

## References

- [A Comprehensive Ultra-Wideband (UWB) Dataset for Non-Cooperative Contextual Sensing](https://figshare.com/collections/A_Comprehensive_Ultra-Wideband_UWB_Dataset_for_Non-Cooperative_Contextual_Sensing/6078021)
- [A comprehensive ultra-wideband dataset for non-cooperative contextual sensing](https://doi.org/10.1038/s41597-022-01776-7)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
