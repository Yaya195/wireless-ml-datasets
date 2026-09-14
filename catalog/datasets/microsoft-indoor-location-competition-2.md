<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Microsoft Indoor Location Competition 2.0 Dataset

**Aliases:** Indoor Location & Navigation, Indoor Location Competition 2.0

A large-scale multi-building indoor localization benchmark containing smartphone Wi-Fi scans, Bluetooth iBeacon observations, inertial and geomagnetic measurements, floor plans, and waypoint ground truth collected across hundreds of buildings.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi RSSI, RSS, IMU, Geomagnetic field, Position, Scene geometry |
| Technologies | Wi-Fi, BLE |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor |
| Mobility | Mobile |
| Temporal structure | Trajectory |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz

Wi-Fi scan records include per-access-point frequency and Bluetooth iBeacon measurements operate in the 2.4 GHz ISM band; the resource spans many buildings and deployments.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** Wi-Fi RSSI, RSS, IMU, Geomagnetic field, Scene geometry

**Targets:** Position, Floor

**Scope:** Multi-building indoor pedestrian localization and floor estimation from smartphone radio, inertial, geomagnetic, and map observations.

**Task context:** Environment: Indoor · Mobility: Mobile · Frequency: Sub-6 GHz

The benchmark was explicitly released for indoor location and navigation and includes waypoint ground truth.

## Scale

- **Sites:** 204
- **Size (GB):** 60.0
- **Notes:** The ACM MobiCom 2023 competition analysis reports a 60 GB training dataset collected from 204 diverse buildings.

## Resources

- [Dataset access](https://www.kaggle.com/c/indoor-location-navigation/data)
- [Official homepage](https://www.microsoft.com/en-us/research/publication/indoor-location-competition-2-0-dataset/)
- [Official repository](https://github.com/location-competition/indoor-location-competition-20)

## Caveats

- Full-data access is mediated through Kaggle, while the GitHub repository contains only sample traces and supporting code.
- The competition title uses “Navigation”, but the released benchmark is evaluated as indoor location/floor prediction; do not infer a radio-assisted-navigation task mapping without a demonstrated path, waypoint, or action-selection use.

## References

- [Indoor Location Competition 2.0 Dataset — Microsoft Research](https://www.microsoft.com/en-us/research/publication/indoor-location-competition-2-0-dataset/)
- [Indoor Location Competition 2.0 — Sample Data and Code](https://github.com/location-competition/indoor-location-competition-20)
- [Indoor Location & Navigation — Kaggle](https://www.kaggle.com/c/indoor-location-navigation)
- [The Wisdom of 1,170 Teams: Lessons and Experiences from a Large Indoor Localization Competition](https://doi.org/10.1145/3570361.3592507)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
