<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RSRPSet_urban

**Aliases:** RSRPSet urban: Radio map in dense urban

A measured dense-urban RSRP radio-map dataset derived from Huawei-provided field measurements, with hundreds of thousands of receiving locations across roughly 180 communication cells.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Radio map, Position, RSS |
| Technologies | — |
| Generation context | 4G, 5G |
| Radio configuration | — |
| Environment | Outdoor, Urban |
| Mobility | Not applicable |
| Temporal structure | Snapshot |
| Access | Restricted |
| License | Not Reported |

## Frequency

**Status:** Varies

The measured urban cells span multiple radio conditions; one catalogue-wide carrier is not assigned.

## Supported wireless tasks

### [Radio Map Estimation](../tasks/radio-map-estimation.md)

**Inputs:** Radio map, Position

**Targets:** Radio map

**Scope:** Estimate dense-urban cell-level RSRP radio maps from sparse measured radio observations and spatial context.

**Task context:** Environment: Outdoor, Urban · Mobility: Not applicable

## Scale

- **Samples:** 415,244
- **Scenarios:** 181
- **Notes:** Published summaries report 415,244 receiving locations in approximately 181 dense urban cells.

## Resources

- [Dataset access](https://doi.org/10.21227/VMW5-C226)
- [Official homepage](https://github.com/ZhengSaber/Cell-Level-RSRP-Estimation)

## Caveats

- The resource contains measured cell-level RSRP values rather than raw PHY channel measurements.

## References

- [Cell-Level RSRP Estimation](https://github.com/ZhengSaber/Cell-Level-RSRP-Estimation)
- [RSRPSet_urban: Radio map in dense urban](https://doi.org/10.21227/VMW5-C226)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
