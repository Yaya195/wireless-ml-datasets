<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# WAIR-D

**Aliases:** Wireless AI Research Dataset

A large wireless-AI research dataset with channels and environmental information from 10,000 sparse and 100 dense deployment environments selected from maps of more than 40 cities.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Ray tracing |
| Modalities | Channel matrix, Scene geometry, Position, Beam power |
| Technologies | — |
| Generation context | — |
| Radio configuration | Massive MIMO |
| Environment | Outdoor, Urban |
| Mobility | Not applicable |
| Temporal structure | Snapshot |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

Frequency/configuration varies with the dataset generation settings described by the authors.

## Supported wireless tasks

### [Beam Prediction](../tasks/beam-prediction.md)

**Inputs:** Channel matrix, Scene geometry, Position

**Targets:** Beam power

**Scope:** Predict unmeasured spatial beam quality from sparse wireless observations across diverse environments.

**Task context:** Environment: Outdoor, Urban · Mobility: Not applicable

The original WAIR-D paper explicitly demonstrates spatial beam prediction.

## Scale

- **Scenarios:** 10,100
- **Notes:** Scenario 1 has 10,000 environments with sparse UEs; Scenario 2 has 100 dense environments drawn from 40+ cities.

## Resources

- [Dataset access](https://www.mobileai-dataset.com/html/default/yingwen/DateSet/1590994253188792322.html?index=1)
- [Documentation](https://arxiv.org/abs/2212.02159)

## Caveats

- WAIR-D is generated rather than measured over-the-air; its key advantage is environmental diversity at large scale.

## References

- [WAIR-D: Wireless AI Research Dataset](https://arxiv.org/abs/2212.02159)
- [WAIR-D download portal](https://www.mobileai-dataset.com/html/default/yingwen/DateSet/1590994253188792322.html?index=1)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
