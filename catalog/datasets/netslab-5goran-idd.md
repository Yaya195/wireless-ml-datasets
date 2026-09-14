<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# NetsLab-5GORAN-IDD

**Aliases:** 5G Open Radio Access Network Multi-Modal Intrusion Detection Dataset

A multi-modal 5G O-RAN intrusion/anomaly dataset containing lower-layer radio telemetry and network-layer packet traces for benign traffic plus DoS, DDoS, probe, brute-force, and web attacks.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Network KPI, Packet trace |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Indoor, Laboratory |
| Mobility | Not reported |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

## Supported wireless tasks

### [Network Anomaly Detection](../tasks/network-anomaly-detection.md)

**Inputs:** Network KPI, Packet trace

**Targets:** Anomaly label

**Scope:** Detect malicious/anomalous 5G O-RAN operating periods from radio telemetry and/or network traffic.

**Task context:** Environment: Indoor, Laboratory · Mobility: Not reported

Attack categories are treated as malicious network anomalies within the existing catalogue task rather than creating a separate cybersecurity taxonomy.

## Scale

- **Size (GB):** 16.8
- **Notes:** The release includes benign plus five attack-category folders, lower-layer telemetry, PCAP traffic, and summary databases.

## Resources

- [Dataset access](https://zenodo.org/records/18923275)

## Caveats

- The attacks are generated on a controlled O-RAN testbed; deployment-specific attack distributions and benign traffic can differ materially.

## References

- [5G Open Radio Access Network Multi-Modal Intrusion Detection Dataset (NetsLab-5GORAN-IDD)](https://zenodo.org/records/18923275)
- [Descriptor: 5G Open Radio Access Network Multi-Modal Intrusion Detection Dataset (NetsLab-5GORAN-IDD)](https://doi.org/10.1109/IEEEDATA.2025.3614167)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
