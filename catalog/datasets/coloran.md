<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# ColO-RAN Dataset

Colosseum O-RAN measurements for ML-based closed-loop control with seven base stations, 42 UEs, three network slices, three scheduling policies, and many per-slice RBG allocations.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Hybrid |
| Modalities | Network KPI, Traffic |
| Technologies | LTE |
| Generation context | — |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Open |
| License | GNU GPL v3 |

## Frequency

**Status:** Not Reported

## Supported wireless tasks

### [Resource Allocation](../tasks/resource-allocation.md)

**Inputs:** Network KPI, Traffic

**Targets:** —

**Scope:** Learn closed-loop slice resource allocation from RAN measurements under alternative RBG allocations and scheduling policies.

**Task context:** Environment: Laboratory · Mobility: Static

### [User Scheduling](../tasks/user-scheduling.md)

**Inputs:** Network KPI, Traffic

**Targets:** —

**Scope:** Learn or evaluate scheduling-policy selection for network slices from current RAN state.

**Task context:** Environment: Laboratory · Mobility: Static

## Scale

- **Devices:** 42
- **Sites:** 7
- **Notes:** Seven BSs, 42 UEs, three slices and multiple scheduling/RBG configurations are documented by the release.

## Resources

- [Dataset access](https://github.com/wineslab/colosseum-oran-coloran-dataset)

## Caveats

- The measurements come from the programmable Colosseum emulator/testbed rather than a commercial field deployment.

## References

- [Colosseum O-RAN ColORAN Dataset](https://github.com/wineslab/colosseum-oran-coloran-dataset)
- [ColO-RAN: Developing Machine Learning-based xApps for Open RAN Closed-loop Control on Programmable Experimental Platforms](https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=ColO-RAN)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
