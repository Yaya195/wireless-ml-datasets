<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# UNICORN O-RAN KPI Dataset

**Aliases:** UNICORN

A 5G/O-RAN network-traffic dataset containing 492 traces from six mobile applications, released as packet captures/metadata and as time-varying RAN KPI traces after Colosseum processing.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Hybrid |
| Modalities | Packet trace, Network KPI |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Indoor, Outdoor |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

The released task is network/KPI classification rather than RF-frequency characterization.

## Supported wireless tasks

### [Traffic Classification](../tasks/traffic-classification.md)

**Inputs:** Packet trace, Network KPI

**Targets:** Application label

**Scope:** Classify six mobile application classes from network traces or privacy-preserving RAN KPI sequences.

**Task context:** Environment: Indoor, Outdoor · Mobility: Mixed

The paper's primary KPI-based formulation uses 17 RAN KPIs and does not require user payload exposure.

## Scale

- **Sequences:** 492
- **Scenarios:** 3
- **Notes:** 492 traces cover six applications. The processed KPI representation contains 17 selected RAN KPIs per time series.

## Resources

- [Dataset access](https://www.genesys-lab.org/unicorn)

## Caveats

- UNICORN provides several processing stages (PCAP, reduced packet metadata, and Colosseum-derived KPI traces); model inputs and privacy properties differ substantially across these representations.

## References

- [UNICORN KPI Dataset for Network Traffic Classification in O-RAN](https://www.genesys-lab.org/unicorn)
- [URLLC network traces collected for UNICORN](https://doi.org/10.18738/T8/FJXA40)
- [UNICORN: URLLC Network Traffic Classification and OOD Detection for O-RAN](https://genesys-lab.org/papers/Unicorn-genesys.pdf)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
