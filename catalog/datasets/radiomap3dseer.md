<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RadioMap3DSeer

A 3D-aware urban pathloss radio-map dataset extending the RadioMapSeer setting with varying building heights and rooftop transmitter elevations, used in the ICASSP 2023 Pathloss Radio Map Prediction Challenge.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Ray tracing |
| Modalities | Scene geometry, Radio map, Position |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Outdoor, Urban |
| Mobility | Not applicable |
| Temporal structure | Snapshot |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 3.5 GHz

Published descriptions of RadioMap3DSeer use a 3.5 GHz carrier.

## Supported wireless tasks

### [Radio Map Estimation](../tasks/radio-map-estimation.md)

**Inputs:** Scene geometry, Position

**Targets:** Radio map

**Scope:** Predict 3D-aware urban pathloss radio maps from building geometry and transmitter information.

**Task context:** Environment: Outdoor, Urban · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Notes:** The challenge uses 256×256 radio-map images paired with 3D-aware building/transmitter representations.

## Resources

- [Dataset access](https://radiomapchallenge.github.io/dataset.html)

## Caveats

- RadioMap3DSeer is a simulation-based extension of the RadioMapSeer setting; it should be treated as a distinct related dataset rather than as measured field data.

## References

- [The First Pathloss Radio Map Prediction Challenge - Dataset](https://radiomapchallenge.github.io/dataset.html)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
