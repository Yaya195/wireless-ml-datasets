<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# BLE RSSI Dataset for Indoor Localization and Navigation

BLE iBeacon RSSI measurements collected in an operational university library, with labeled location observations and additional unlabeled measurements for indoor localization/navigation research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | RSS |
| Technologies | BLE |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Open |
| License | CC BY 4.0 |

## Frequency

**Status:** Not Reported

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** RSS

**Targets:** Position

**Scope:** Infer indoor location labels from RSSI readings of 13 BLE iBeacons.

**Task context:** Environment: Indoor · Mobility: Static

## Scale

- **Samples:** 6,611
- **Notes:** 1,420 labeled and 5,191 unlabeled instances; 13 iBeacon RSSI features.

## Resources

- [Dataset access](https://archive.ics.uci.edu/dataset/435/ble%2Brssi%2Bdataset%2Bfor%2Bindoor%2Blocalization%2Band%2Bnavigation)

## Caveats

- The labeled target is a discrete grid/location identifier rather than continuous metric coordinates.

## References

- [BLE RSSI Dataset for Indoor localization and Navigation](https://archive.ics.uci.edu/dataset/435/ble%2Brssi%2Bdataset%2Bfor%2Bindoor%2Blocalization%2Band%2Bnavigation)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
