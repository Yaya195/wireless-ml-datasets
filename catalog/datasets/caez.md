<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# CAEZ

**Aliases:** CSI Acquisition at ETH Zurich

A real-world CSI collection from ETH Zurich 5G NR and distributed Wi-Fi testbeds, including position-tagged indoor, outdoor, hallway, and multi-campaign measurements.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Channel matrix, Position |
| Technologies | Wi-Fi, 5G NR |
| Generation context | 5G |
| Radio configuration | MIMO |
| Environment | Indoor, Outdoor, Campus, Office |
| Mobility | Mobile |
| Temporal structure | Trajectory |
| Access | Open |
| License | CAEZ Dataset License v1.0 |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 3.45 GHz (5G NR n78), 5 GHz Wi-Fi

CAEZ-5G uses 100 MHz of the Swiss private 5G n78 band centered at 3.45 GHz; CAEZ-WIFI uses active 5 GHz Wi-Fi networks.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** Channel matrix

**Targets:** Position

**Scope:** Multiple CAEZ-5G and CAEZ-WIFI campaigns provide CSI aligned with ground-truth UE positions for neural positioning.

**Task context:** Environment: Indoor, Outdoor, Campus, Office · Mobility: Mobile · Frequency: Sub-6 GHz

### [Channel Charting](../tasks/channel-charting.md)

**Inputs:** Channel matrix

**Targets:** —

**Evaluation reference:** Position

**Scope:** CAEZ explicitly supports channel charting, including charting in real-world coordinates for position-tagged CSI.

**Task context:** Environment: Indoor, Outdoor, Campus · Mobility: Mobile · Frequency: Sub-6 GHz

Position labels are geometric reference/evaluation information for the learned chart; position is not an intrinsic channel-charting output.

## Scale

- **Scenarios:** 6
- **Notes:** The official collection currently lists four CAEZ-5G datasets and two CAEZ-WIFI datasets.

## Resources

- [Dataset access](https://iip.ethz.ch/datasets/caez.html)

## Caveats

- CAEZ combines distinct 5G NR and Wi-Fi campaigns with different hardware, bandwidths, positioning systems, and acquisition protocols; users should select the appropriate sub-dataset rather than treating the collection as homogeneous.

## References

- [CAEZ: CSI Acquisition at ETH Zurich](https://iip.ethz.ch/datasets/caez.html)
- [CSI-Based User Positioning, Channel Charting, and Device Classification with an NVIDIA 5G Testbed](https://arxiv.org/abs/2512.10809)
- [A Software-Defined and Distributed Wi-Fi Channel-State Information Acquisition Testbed](https://arxiv.org/abs/2412.07588)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
