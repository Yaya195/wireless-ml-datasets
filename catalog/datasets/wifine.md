<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# WiFine

**Aliases:** Finer-level Sequential WiFi-based Indoor Localization Dataset

A sequential Wi-Fi RSS indoor-localization dataset with 290 trajectories collected over three floors of Nazarbayev University's C4 building, with fine-grained 3D position coordinates.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi RSSI, Position |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Campus |
| Mobility | Mobile |
| Temporal structure | Trajectory |
| Access | Open |
| License | MIT License |

## Frequency

**Status:** Not Reported

The public dataset card does not establish one collection-wide carrier value.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** Wi-Fi RSSI

**Targets:** Position

**Scope:** Estimate sequential indoor 3D position from Wi-Fi RSS fingerprints along trajectories.

**Task context:** Environment: Indoor, Campus · Mobility: Mobile

## Scale

- **Samples:** 25,790
- **Sequences:** 290
- **Sites:** 1
- **Duration (hours):** 42.14
- **Notes:** Three floors, 436 WAPs, 9,564 m² and about 42.8 km of total trajectories.

## Resources

- [Dataset access](https://huggingface.co/datasets/issai/WiFine)
- [Official repository](https://github.com/IS2AI/WiFine)

## Caveats

- All trajectories come from one three-floor university building, so cross-building generalization is not directly represented.

## References

- [WiFine](https://huggingface.co/datasets/issai/WiFine)
- [Finer-level Sequential WiFi-based Indoor Localization](https://ieeexplore.ieee.org/document/9382623)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
