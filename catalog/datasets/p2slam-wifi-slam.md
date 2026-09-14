<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# P2SLAM Wi-Fi SLAM Dataset Collection

**Aliases:** P²SLAM Dataset, P2SLAM Dataset

A real-world indoor robotics dataset collection for bearing-based Wi-Fi SLAM, combining reciprocal Wi-Fi CSI/RSSI with robot odometry, IMU, camera, LiDAR, AP geometry, and Cartographer-derived pose ground truth across multiple trajectories and environments.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Wi-Fi CSI, RSS, Odometry, IMU, Camera, LiDAR, Position, Scene geometry |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | MIMO |
| Environment | Indoor, Office |
| Mobility | Mobile |
| Temporal structure | Trajectory |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** Wi-Fi channel 36

The P2SLAM paper reports IEEE 802.11ac channel 36 with 80 MHz bandwidth.

## Supported wireless tasks

### [Radio SLAM](../tasks/radio-slam.md)

**Inputs:** Wi-Fi CSI, Odometry

**Targets:** Position, Orientation / heading, Scene / environment geometry

**Evaluation reference:** Position, Orientation / heading, Scene / environment geometry

**Scope:** Estimate the robot trajectory and Wi-Fi AP landmark poses from reciprocal Wi-Fi channel-derived bearings fused with odometry in an indoor GraphSLAM system.

**Task context:** Environment: Indoor, Office · Mobility: Mobile · Frequency: Sub-6 GHz

This is a direct SLAM dataset: P2SLAM treats both robot poses and previously unknown Wi-Fi AP poses as optimization variables.

## Scale

- **Sequences:** 3
- **Scenarios:** 3
- **Sites:** 2
- **Size (GB):** 19.6
- **Notes:** The original P2SLAM page distributes three trajectory datasets totaling about 19.6 GB; WAIS later adds another dataset to the project lineage.

## Resources

- [Dataset access](https://wcsng.ucsd.edu/p2slam/)

## Caveats

- Access requires a registration form, and the project distributes a collection of multiple trajectories rather than a single fixed train/test benchmark.

## References

- [P2SLAM: Bearing based WiFi SLAM for Indoor Robots](https://wcsng.ucsd.edu/p2slam/)
- [P2SLAM: Bearing Based WiFi SLAM for Indoor Robots](https://doi.org/10.1109/LRA.2022.3144796)
- [WAIS: Leveraging WiFi for Resource-Efficient SLAM](https://wcsng.ucsd.edu/wais/)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
