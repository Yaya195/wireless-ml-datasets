<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# IMUWiFine

**Aliases:** IMUWiFine: End-to-End Sequential Indoor Localization

A large sequential indoor-localization dataset combining smartphone IMU measurements with Wi-Fi RSSI over 120 trajectories and three floors of Nazarbayev University's C4 building.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | IMU, Wi-Fi RSSI, Position |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Campus |
| Mobility | Mobile |
| Temporal structure | Trajectory |
| Access | Open |
| License | CC BY 4.0 |

## Frequency

**Status:** Not Reported

The public card does not expose one collection-wide Wi-Fi carrier value.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** IMU, Wi-Fi RSSI

**Targets:** Position

**Scope:** Estimate sequential indoor position from jointly observed smartphone IMU and Wi-Fi RSSI.

**Task context:** Environment: Indoor, Campus · Mobility: Mobile

## Scale

- **Samples:** 5,400,000
- **Sequences:** 120
- **Sites:** 1
- **Duration (hours):** 10.4
- **Size (GB):** 30.6
- **Notes:** About 14.2 km of trajectories over more than 9,000 m² across three floors.

## Resources

- [Dataset access](https://huggingface.co/datasets/issai/IMUWiFine)
- [Official repository](https://github.com/IS2AI/IMUWiFine)
- [Documentation](https://huggingface.co/datasets/issai/IMUWiFine/blob/main/README.md)

## Caveats

- The resource covers one building; transfer to unseen buildings must be evaluated separately.

## References

- [IMUWiFine](https://huggingface.co/datasets/issai/IMUWiFine)
- [End-to-End Sequential Indoor Localization Using Smartphone Inertial Sensors and WiFi](https://doi.org/10.1109/SII52469.2022.9708854)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
