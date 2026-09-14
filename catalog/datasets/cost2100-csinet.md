<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# COST2100 CsiNet CSI-Feedback Dataset

**Aliases:** CsiNet COST2100 Data

Preprocessed COST2100 indoor and outdoor massive-MIMO channel matrices released with the original CsiNet implementation for learning compact CSI feedback and reconstruction.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Simulation |
| Modalities | Channel matrix |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor, Outdoor |
| Mobility | Configurable |
| Temporal structure | Snapshot |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

## Supported wireless tasks

### [CSI Feedback](../tasks/csi-feedback.md)

**Inputs:** Channel matrix

**Targets:** Channel

**Scope:** Compress and reconstruct downlink massive-MIMO CSI using the CsiNet/CS-CsiNet benchmark data.

**Task context:** Environment: Indoor, Outdoor · Mobility: Configurable

## Resources

- [Dataset access](https://github.com/sydney222/Python_CsiNet)

## Caveats

- The benchmark is model-generated rather than over-the-air measured; indoor and outdoor subsets correspond to COST2100 scenarios.

## References

- [Python_CsiNet: original code and COST2100 data preparation](https://github.com/sydney222/Python_CsiNet)
- [Deep Learning for Massive MIMO CSI Feedback](https://ieeexplore.ieee.org/document/8322184)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
