<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# ITU 2024 Massive-MIMO Multi-User Scheduling Datasets

**Aliases:** Multi-User Beamforming Scheduling Challenge Datasets

Two massive-MIMO channel datasets released for the ITU 2024 multi-user beamforming scheduling challenge: a low-mobility dataset derived from RENEW measurements and a high-mobility QuaDRiGa/3GPP UMi dataset.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Hybrid |
| Modalities | Channel matrix |
| Technologies | — |
| Generation context | 5G |
| Radio configuration | Massive MIMO |
| Environment | Outdoor, Campus, Urban |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

The challenge documents 52 data-carrying subcarriers and a 20 MHz high-mobility channel, but no single collection-wide carrier is assigned.

## Supported wireless tasks

### [User Scheduling](../tasks/user-scheduling.md)

**Inputs:** Channel matrix

**Targets:** —

**Scope:** Select groups of users per time-frequency resource from massive-MIMO channel estimates to maximize rate while maintaining fairness under mobility.

**Task context:** Environment: Outdoor, Campus, Urban · Mobility: Mixed

Scheduling is formulated as a sequential control/optimization problem rather than fixed-label prediction.

## Scale

- **Sequences:** 2
- **Devices:** 64
- **Notes:** Both datasets contain 64 users; the low-mobility set provides 52 subcarriers over 500 frames.

## Resources

- [Dataset access](https://github.com/ITU-AI-ML-in-5G-Challenge/Challenge_Archive/blob/main/2024/Optimal%20Multi-user%20scheduling%20in%20massive%20MIMO%20mobile%20channels/Readme.md)
- [Official repository](https://github.com/ITU-AI-ML-in-5G-Challenge/Challenge_Archive)

## Caveats

- The two challenge datasets have different provenance and mobility regimes; their results should not be pooled without preserving the low-/high-mobility distinction.

## References

- [Multi-User Beamforming Scheduling Challenge](https://github.com/ITU-AI-ML-in-5G-Challenge/Challenge_Archive/blob/main/2024/Optimal%20Multi-user%20scheduling%20in%20massive%20MIMO%20mobile%20channels/Readme.md)
- [A Deep Reinforcement Learning-Based Resource Scheduler for Massive MIMO Networks](https://doi.org/10.1109/TMLCN.2023.3313988)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
