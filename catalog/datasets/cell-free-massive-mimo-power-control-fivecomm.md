<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Dataset for Power Control in Cell-Free Massive MIMO

A simulated cell-free massive-MIMO dataset spanning 12 scenarios and three power-control objectives, with large-scale fading coefficients, optimized uplink power coefficients, and spectral-efficiency outputs.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Simulation |
| Modalities | Channel matrix |
| Technologies | — |
| Generation context | — |
| Radio configuration | Massive MIMO |
| Environment | Unknown |
| Mobility | Not applicable |
| Temporal structure | Snapshot |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

No single carrier/frequency regime is assigned at catalogue level.

## Supported wireless tasks

### [Power Control](../tasks/power-control.md)

**Inputs:** Channel matrix

**Targets:** Power allocation

**Scope:** Learn uplink power-control coefficients from large-scale fading and interference-related channel statistics under max-min, sum-SE, and fractional-power-control objectives.

**Task context:** Environment: Unknown · Mobility: Not applicable

## Scale

- **Samples:** 240,000
- **Scenarios:** 12
- **Size (GB):** 2.3
- **Notes:** Each of 12 scenarios contains 20,000 independently simulated setups.

## Resources

- [Dataset access](https://zenodo.org/records/10691343)
- [Official repository](https://github.com/Fivecomm/cell-free-power-control-DNN)

## Caveats

- The resource is fully simulation-based and contains several distinct power-control objectives; comparisons should state the scenario and objective used.

## References

- [Dataset for Power Control in Cell-Free Massive MIMO](https://zenodo.org/records/10691343)
- [A Flexible Low-Complexity DNN Solution for Power Control in Cell-Free Massive MIMO](https://doi.org/10.1109/PIMRC59610.2024.10817296)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
