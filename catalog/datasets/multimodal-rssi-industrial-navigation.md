<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Multi-Technology RSSI Dataset for Indoor Positioning and Navigation

**Aliases:** Multimodal RSSI Localization Dataset

A measured Wi-Fi and BLE RSSI dataset collected by an autonomous industrial robot along repeated indoor trajectories, with timestamped position, orientation, linear/angular velocity, anchor coordinates, and trajectory labels in an interference-prone laboratory.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi RSSI, RSS, Position, Scene geometry |
| Technologies | Wi-Fi, BLE |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Laboratory, Industrial |
| Mobility | Mixed |
| Temporal structure | Trajectory |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz

The dataset combines commodity Wi-Fi and BLE RSSI measurements.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** Wi-Fi RSSI, RSS

**Targets:** Position

**Scope:** Indoor Wi-Fi/BLE RSSI positioning and hybrid fingerprinting under repeated trajectories and interference-prone industrial conditions.

**Task context:** Environment: Indoor, Laboratory, Industrial · Mobility: Mixed · Frequency: Sub-6 GHz

The published proof of concept validates positioning/fingerprinting; the richer trajectory annotations also make the resource useful for tracking/navigation research.

## Scale

- **Samples:** 71,576
- **Sequences:** 71
- **Scenarios:** 3
- **Devices:** 30
- **Sites:** 1
- **Notes:** The paper reports 71,576 RSSI measurements; trajectories A, B, and C were traversed 26, 24, and 21 times, respectively, with 30 anchors/devices deployed across 17 positions.

## Resources

- [Dataset access](https://github.com/GiovanniPettorru/multimodal-RSSI-localization-dataset)
- [Documentation](https://doi.org/10.1016/j.future.2026.108634)

## Caveats

- The resource is explicitly described as useful for navigation, but the published proof-of-concept benchmark validates positioning rather than path/waypoint/action selection; it is therefore not mapped to radio-assisted-navigation in V1.

## References

- [Multi-Technology RSSI Dataset for Indoor Positioning and Navigation — repository](https://github.com/GiovanniPettorru/multimodal-RSSI-localization-dataset)
- [A multimodal RSSI-based dataset for indoor navigation in interference-prone environments](https://doi.org/10.1016/j.future.2026.108634)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
