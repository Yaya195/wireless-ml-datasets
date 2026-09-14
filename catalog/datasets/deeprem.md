<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# DeepREM Urban REM Dataset

**Aliases:** DeepREM

An urban radio-environment-map dataset generated from topography, building vector data, and intelligent ray tracing across multiple Colombian and U.S. cities, released for deep-learning REM estimation from sparse measurements.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Ray tracing |
| Modalities | Radio map, Scene geometry |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Outdoor, Urban |
| Mobility | Not applicable |
| Temporal structure | Snapshot |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

The verified dataset landing page does not establish one carrier for the full collection.

## Supported wireless tasks

### [Radio Map Estimation](../tasks/radio-map-estimation.md)

**Inputs:** Radio map, Scene geometry

**Targets:** Radio map

**Scope:** Estimate complete urban radio environment maps from sparse radio-map observations and spatial context.

**Task context:** Environment: Outdoor, Urban · Mobility: Not applicable

The release accompanies U-Net and CGAN methods for REM reconstruction from sparse measurements.

## Scale

- **Size (GB):** 0.883
- **Notes:** The main urban REM archive is about 830 MB plus test data; the second release adds 400 maps across four additional city areas.

## Resources

- [Dataset access](https://zenodo.org/records/7839447)

## Caveats

- DeepREM maps are ray-tracing-based urban simulations rather than measured drive-test radio maps.

## References

- [DeepREM: Deep-Learning-Based Radio Environment Map Estimation from Sparse Measurements](https://zenodo.org/records/7839447)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
