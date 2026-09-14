<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Colosseum O-RAN COMMAG Dataset

An O-RAN/Colosseum dataset of per-slice RAN measurements collected under different scheduling policies, resource-block allocations, traffic classes, RF conditions, and UE mobility settings.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Hybrid |
| Modalities | Network KPI, Traffic |
| Technologies | LTE |
| Generation context | 4G, 5G |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | GNU GPL v3 |

## Frequency

**Status:** Not Reported

The public repository describes a 3 MHz / 15-PRB experimental cellular setup but does not expose one canonical RF carrier for the collection.

## Supported wireless tasks

### [Resource Allocation](../tasks/resource-allocation.md)

**Inputs:** Network KPI, Traffic

**Targets:** —

**Scope:** Learn or evaluate dynamic per-slice radio-resource decisions from RAN state under varying scheduler and RBG configurations.

**Task context:** Environment: Laboratory · Mobility: Mixed

The released PPO agents use RAN measurements to select actions that optimize slice-specific throughput or latency objectives.

## Scale

- **Devices:** 40
- **Notes:** The documented setup includes 4 base stations, 40 UEs, 3 slices, 3 scheduler families, and multiple RBG allocations.

## Resources

- [Dataset access](https://github.com/wineslab/colosseum-oran-commag-dataset)

## Caveats

- The dataset is produced on the Colosseum wireless network emulator; it provides controlled, repeatable RAN experiments but is not equivalent to a commercial-network field trace.

## References

- [Colosseum O-RAN COMMAG Dataset](https://github.com/wineslab/colosseum-oran-commag-dataset)
- [Intelligence and Learning in O-RAN for Data-driven NextG Cellular Networks](https://ieeexplore.ieee.org/document/9627832)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
