<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# e-FLASH V2X Beam-Selection Dataset

**Aliases:** SMART Sim2Real mmWave Beam Selection Dataset

A real-world multimodal V2X dataset with synchronized LiDAR, camera, GPS and wireless-connectivity data across LOS and several NLOS obstacle scenarios for mmWave beam selection and sim-to-real learning.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | LiDAR, Camera, Position, Beam power |
| Technologies | — |
| Generation context | 5G |
| Radio configuration | Phased array |
| Environment | Outdoor, Vehicular |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** mmWave

The project explicitly targets mmWave V2X beam selection.

## Supported wireless tasks

### [Beam Selection](../tasks/beam-selection.md)

**Inputs:** LiDAR, Camera, Position, Beam power

**Targets:** Beam index

**Scope:** Select mmWave V2X beams from synchronized LiDAR, camera, GPS and wireless-connectivity observations.

**Task context:** Environment: Outdoor, Vehicular · Mobility: Mixed · Frequency: mmWave

## Scale

- **Samples:** 10,853
- **Size (GB):** 22.0
- **Notes:** The real-world e-FLASH component contains 10,853 processed samples.

## Resources

- [Dataset access](https://genesys-lab.org/smart)
- [Official repository](https://github.com/genesys-neu/FLASH-MAML)

## Caveats

- The SMART framework also uses synthetic S-FLASH data; this record describes the real-world e-FLASH component.

## References

- [SMART: Sim2Real Meta-Learning-based Training for mmWave Beam Selection in V2X Networks](https://genesys-lab.org/smart)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
