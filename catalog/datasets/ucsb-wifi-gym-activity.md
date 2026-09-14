<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# WiFi CSI Dataset of Common Physical Exercises

**Aliases:** WiFi Gym Activity Dataset

A measured Wi-Fi CSI human-activity dataset with 300 activity periods from 10 participants performing 10 physical exercises across three indoor environments.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | MIMO |
| Environment | Indoor, Laboratory |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Available on request |
| License | CC BY-NC 4.0 |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 5.18 GHz / 5.22 GHz

The associated experiments use Wi-Fi channels 36 and 44 at 5.18 and 5.22 GHz.

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI

**Targets:** Activity label

**Scope:** Classify ten physical exercises from real Wi-Fi CSI measurements.

**Task context:** Environment: Indoor, Laboratory · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Samples:** 300
- **Scenarios:** 3
- **Participants:** 10
- **Notes:** Ten participants perform ten activities in three environments, yielding 300 activity periods.

## Resources

- [Dataset access](https://web.ece.ucsb.edu/mostofi-lab/WiFiGymActivityDataset.html)

## Caveats

- The dataset contains only 10 participants and three environments and is distributed by request rather than direct public download.

## References

- [WiFi CSI Dataset of Common Physical Exercises](https://web.ece.ucsb.edu/mostofi-lab/WiFiGymActivityDataset.html)
- [Teaching RF to Sense without RF Training Measurements](https://doi.org/10.1145/3432224)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
