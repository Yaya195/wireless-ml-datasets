<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# 5G-NIDD

**Aliases:** 5G Wireless Network Intrusion Detection Dataset

A fully labelled intrusion-detection dataset collected on the University of Oulu 5G Test Network, with benign traffic and multiple DoS and port-scan attacks.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Packet trace |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Not reported |
| Temporal structure | Sequence |
| Access | Open |
| License | CC BY 4.0 |

## Frequency

**Status:** Not Reported

## Supported wireless tasks

### [Network Anomaly Detection](../tasks/network-anomaly-detection.md)

**Inputs:** Packet trace

**Targets:** Anomaly label

**Scope:** Detect malicious or anomalous 5G network traffic across documented DoS and port-scan scenarios.

**Task context:** Environment: Laboratory · Mobility: Not reported

Intrusion detection is represented under the existing network-anomaly-detection task.

## Scale

- **Scenarios:** 8
- **Notes:** Eight documented attack scenarios cover five DoS variants and three port scans, in addition to benign traffic.

## Resources

- [Dataset access](https://doi.org/10.23729/e80ac9df-d9fb-47e7-8d0d-01384a415361)
- [Official repository](https://github.com/yushan1986/5g-nidd)
- [Documentation](https://doi.org/10.21227/xtep-hv36)

## Caveats

- The attack traffic was generated on a controlled 5G test network, so deployment-specific benign and malicious traffic distributions may differ.

## References

- [5G-NIDD](https://doi.org/10.23729/e80ac9df-d9fb-47e7-8d0d-01384a415361)
- [5G-NIDD: A Comprehensive Network Intrusion Detection Dataset Generated over 5G Wireless Network](https://doi.org/10.21227/xtep-hv36)
- [Descriptor: 5G Wireless Network Intrusion Detection Dataset (5G-NIDD)](https://doi.org/10.1109/IEEEDATA.2025.3592888)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-10-20`
