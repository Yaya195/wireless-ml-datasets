<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# DICHASUS

**Aliases:** DICHASUS Massive MIMO CSI Dataset Collection

A collection of real, phase-coherent massive-MIMO CSI measurements with position ground truth across indoor, outdoor, colocated, and distributed-antenna scenarios.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Channel matrix, Position |
| Technologies | — |
| Generation context | — |
| Radio configuration | MIMO, Massive MIMO |
| Environment | Indoor, Outdoor, Campus, Industrial |
| Mobility | Mixed |
| Temporal structure | Mixed |
| Access | Open |
| License | Varies |

## Frequency

**Regimes:** Sub-6 GHz

Carrier frequency and bandwidth vary by measurement campaign; individual dataset pages provide exact values.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** Channel matrix

**Targets:** Position

**Scope:** CSI-based positioning is demonstrated on indoor position-tagged DICHASUS measurements.

**Task context:** Environment: Indoor · Mobility: Mobile · Frequency: Sub-6 GHz

### [Channel Charting](../tasks/channel-charting.md)

**Inputs:** Channel matrix

**Targets:** —

**Evaluation reference:** Position

**Scope:** Measured CSI is used to learn radio-geometric low-dimensional charts; position labels support evaluation.

**Task context:** Environment: Indoor · Mobility: Mobile · Frequency: Sub-6 GHz

Position labels are geometric reference/evaluation information for the learned chart; position is not an intrinsic channel-charting output.

## Scale

- **Notes:** The collection contains multiple independently DOI-identified measurement campaigns and continues to evolve.

## Resources

- [Dataset access](https://dichasus.inue.uni-stuttgart.de/)
- [Documentation](https://dichasus.inue.uni-stuttgart.de/tutorials/)

## Caveats

- DICHASUS is a collection of separate measurement campaigns; scenario-specific frequency, antenna geometry, and ground-truth quality must be checked before comparing results across campaigns.

## References

- [DICHASUS Massive MIMO CSI Dataset Collection](https://dichasus.inue.uni-stuttgart.de/)
- [DICHASUS Positioning Tutorial](https://dichasus.inue.uni-stuttgart.de/tutorials/tutorial/positioning/)
- [DICHASUS Dissimilarity Metric-Based Channel Charting](https://dichasus.inue.uni-stuttgart.de/tutorials/tutorial/dissimilarity-metric-channelcharting/)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
