<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Simulated CSI for 6G In-Factory Subnetworks

**Aliases:** ITU Radio Resource Management for 6G In-X Subnetworks Dataset

A simulated dense industrial In-X subnetwork CSI dataset released for the ITU AI/ML challenge on joint sub-band and transmit-power allocation.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Simulation |
| Modalities | Channel matrix, Position |
| Technologies | 6G |
| Generation context | 6G |
| Radio configuration | — |
| Environment | Indoor, Industrial |
| Mobility | Configurable |
| Temporal structure | Snapshot |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 6 GHz

The challenge setup uses a 6 GHz carrier and 10 MHz system bandwidth.

## Supported wireless tasks

### [Power Control](../tasks/power-control.md)

**Inputs:** Channel matrix, Position

**Targets:** —

**Scope:** Determine transmit-power levels jointly with frequency-resource decisions for dense 6G In-X subnetworks from channel/network state.

**Task context:** Environment: Indoor, Industrial · Mobility: Configurable · Frequency: Sub-6 GHz

This is an optimization/control formulation; no fixed supervised power label is treated as intrinsic ground truth.

### [Resource Allocation](../tasks/resource-allocation.md)

**Inputs:** Channel matrix, Position

**Targets:** —

**Scope:** Perform joint sub-band and power allocation to maximize network spectral efficiency under interference constraints.

**Task context:** Environment: Indoor, Industrial · Mobility: Configurable · Frequency: Sub-6 GHz

## Scale

- **Samples:** 200,000
- **Devices:** 20
- **Size (GB):** 2.5
- **Notes:** The challenge dataset contains 200,000 snapshots for 20 in-factory subnetworks and four sub-bands.

## Resources

- [Dataset access](https://zenodo.org/records/10908382)
- [Official repository](https://github.com/ITU-AI-ML-in-5G-Challenge/Challenge_Archive/tree/main/2024/Radio%20Resource%20Management%20%28RRM%29%20for%206G%20in-X%20Subnetworks%20%5Bxtended%5D)
- [Documentation](https://github.com/ITU-AI-ML-in-5G-Challenge/Challenge_Archive/blob/main/2024/Radio%20Resource%20Management%20%28RRM%29%20for%206G%20in-X%20Subnetworks%20%5Bxtended%5D/Readme.md)

## Caveats

- The dataset is simulated and challenge-specific; its operational constraints should be preserved when comparing learned RRM policies.

## References

- [Simulated Channel state information for In-factory Subnetworks](https://zenodo.org/records/10908382)
- [AI/ML for Radio Resource Management in Hyper-Dense In-X Subnetworks](https://github.com/ITU-AI-ML-in-5G-Challenge/Challenge_Archive/blob/main/2024/Radio%20Resource%20Management%20%28RRM%29%20for%206G%20in-X%20Subnetworks%20%5Bxtended%5D/Readme.md)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
