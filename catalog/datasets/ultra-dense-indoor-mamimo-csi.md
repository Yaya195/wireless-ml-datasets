<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Ultra Dense Indoor MaMIMO CSI Dataset

**Aliases:** Ultra-Dense Indoor Massive MIMO CSI Dataset

A measured ultra-dense indoor massive-MIMO CSI dataset from a 64-antenna KU Leuven testbed, with four antenna-array topologies and high-precision 2D spatial labels over a 9 m² area.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Channel matrix, Position |
| Technologies | — |
| Generation context | 5G |
| Radio configuration | Massive MIMO |
| Environment | Indoor, Laboratory |
| Mobility | Static |
| Temporal structure | Snapshot |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Status:** Not Reported

No catalogue-wide carrier value is assigned without relying on a secondary description.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** Channel matrix

**Targets:** Position

**Scope:** Estimate indoor 2D user position from measured massive-MIMO CSI under multiple array topologies.

**Task context:** Environment: Indoor, Laboratory · Mobility: Static

## Scale

- **Samples:** 1,008,016
- **Notes:** 252,004 labeled CSI samples are reported for each of four measured array/topology conditions.

## Resources

- [Dataset access](https://ieee-dataport.org/open-access/ultra-dense-indoor-mamimo-csi-dataset)
- [Official homepage](https://www.esat.kuleuven.be/wavecorearenberg/research/NetworkedSystems/datasets)
- [Official repository](https://github.com/sibrendebast/MaMIMO-CSI-positioning-using-CNNs)

## Caveats

- The dense spatial labels come from one controlled indoor testbed; topology-specific and cross-site generalization should be reported separately.

## References

- [KU Leuven Networked Systems Datasets](https://www.esat.kuleuven.be/wavecorearenberg/research/NetworkedSystems/datasets)
- [Ultra Dense Indoor MaMIMO CSI Dataset](https://ieee-dataport.org/open-access/ultra-dense-indoor-mamimo-csi-dataset)
- [MaMIMO CSI positioning using CNNs](https://github.com/sibrendebast/MaMIMO-CSI-positioning-using-CNNs)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
