<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# NIST AdapShare Dataset

**Aliases:** AdapShare

A NIST dataset and code release for reinforcement-learning-based dynamic spectrum/resource sharing between LTE and 5G NR in an O-RAN-compatible architecture.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Hybrid |
| Modalities | Network KPI, Traffic |
| Technologies | LTE, 5G NR |
| Generation context | 4G, 5G |
| Radio configuration | — |
| Environment | Campus |
| Mobility | Not reported |
| Temporal structure | Sequence |
| Access | Open |
| License | NIST Open License |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** LTE Band 4 downlink around 2115 MHz

The documented real LTE scheduling data were collected from downlink traffic around 2115 MHz; the broader sharing study includes LTE and NR.

## Supported wireless tasks

### [Resource Allocation](../tasks/resource-allocation.md)

**Inputs:** Network KPI, Traffic

**Targets:** —

**Scope:** Learn dynamic LTE/NR spectrum-resource allocation policies from time-varying demand and scheduling state.

**Task context:** Environment: Campus · Mobility: Not reported · Frequency: Sub-6 GHz

The released study formulates dynamic spectrum sharing as an RL control problem rather than supervised prediction of a fixed label.

## Scale

- **Notes:** The public release contains data and code used for the AdapShare evaluation; raw LTE scheduling logs include per-subframe allocation and control information.

## Resources

- [Dataset access](https://data.nist.gov/od/id/mds2-3613)
- [Official repository](https://github.com/usnistgov/AdapShare-An-RL-Based-Dynamic-Spectrum-Sharing-Solution-for-O-RAN)
- [Documentation](https://catalog.data.gov/dataset/adapshare-an-rl-based-dynamic-spectrum-sharing-solution-for-o-ran)

## Caveats

- AdapShare combines measured LTE scheduling information with modeled/synthetic components for LTE/NR sharing; it should therefore be treated as a hybrid rather than purely field-measured dataset.

## References

- [AdapShare: An RL-Based Dynamic Spectrum Sharing Solution for O-RAN](https://data.nist.gov/od/id/mds2-3613)
- [AdapShare code and data collection documentation](https://github.com/usnistgov/AdapShare-An-RL-Based-Dynamic-Spectrum-Sharing-Solution-for-O-RAN)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
