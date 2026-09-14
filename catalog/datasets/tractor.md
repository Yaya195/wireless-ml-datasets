<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# TRACTOR Open RAN Traffic Dataset

**Aliases:** TRACTOR

A public 5G/Open-RAN traffic dataset containing real smartphone packet traces and Colosseum-derived O-RAN KPI logs for traffic-slice/application classification.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Hybrid |
| Modalities | Packet trace, Network KPI |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Indoor, Outdoor, Campus, Residential |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | MIT License |

## Frequency

**Status:** Not Reported

The classification resource is represented at packet/KPI level rather than by one RF carrier.

## Supported wireless tasks

### [Traffic Classification](../tasks/traffic-classification.md)

**Inputs:** Packet trace, Network KPI

**Targets:** Application label

**Scope:** Classify network traffic/slice type from packet traces or O-RAN KPI time series.

**Task context:** Environment: Indoor, Outdoor, Campus, Residential · Mobility: Mixed

## Scale

- **Duration (hours):** 7.45
- **Notes:** The official description reports 447 minutes of real 5G user traffic.

## Resources

- [Dataset access](https://github.com/genesys-neu/TRACTOR)
- [Official homepage](https://genesys-lab.org/tractor)

## Caveats

- TRACTOR exposes both packet-level and KPI-level representations; experiments should state which processing stage is used.

## References

- [TRACTOR: Traffic Analysis and Classification Tool for Open RAN](https://genesys-lab.org/tractor)
- [TRACTOR repository](https://github.com/genesys-neu/TRACTOR)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
