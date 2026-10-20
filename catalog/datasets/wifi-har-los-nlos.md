<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Wi-Fi HAR in LOS and NLOS Indoor Environments

**Aliases:** A dataset for Wi-Fi-based human activity recognition in line-of-sight and non-line-of-sight indoor environments

A measured Wi-Fi CSI/RSSI human-activity dataset collected from 30 participants across three indoor environments spanning line-of-sight and non-line-of-sight conditions.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi CSI, Wi-Fi RSSI |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | CC BY 4.0 |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 2.4 GHz Wi-Fi channel 3

The acquisition used 20 MHz bandwidth and a sampling rate of 320 packets per second.

## Supported wireless tasks

### [Human Activity Recognition](../tasks/human-activity-recognition.md)

**Inputs:** Wi-Fi CSI, Wi-Fi RSSI

**Targets:** Activity label

**Scope:** Recognize five human activities from Wi-Fi CSI and RSSI across LOS and NLOS indoor environments.

**Task context:** Environment: Indoor · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Sequences:** 3,000
- **Scenarios:** 3
- **Participants:** 30
- **Sites:** 3
- **Notes:** In each environment, ten participants performed five activities with twenty trials per activity, for 3,000 trials overall.

## Resources

- [Dataset access](https://data.mendeley.com/datasets/v38wjmz6f6/2)
- [Official repository](https://github.com/lcsig/Dataset-for-Wi-Fi-based-human-activity-recognition-in-LOS-and-NLOS-indoor-environments)
- [Documentation](https://doi.org/10.1016/j.dib.2020.106534)

## Caveats

- LOS was used in the first two environments and NLOS in the third, so propagation condition and collection environment are not independently varied.

## References

- [A dataset for Wi-Fi-based human activity recognition in line-of-sight and non-line-of-sight indoor environments](https://data.mendeley.com/datasets/v38wjmz6f6/2)
- [A dataset for Wi-Fi-based human activity recognition in line-of-sight and non-line-of-sight indoor environments](https://doi.org/10.1016/j.dib.2020.106534)
- [Dataset for Wi-Fi-based human activity recognition in LOS and NLOS indoor environments](https://github.com/lcsig/Dataset-for-Wi-Fi-based-human-activity-recognition-in-LOS-and-NLOS-indoor-environments)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-10-20`
