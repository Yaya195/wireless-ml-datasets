<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# SpotLight Open RAN Anomaly Dataset

**Aliases:** SpotLight Dataset

A labeled Open RAN anomaly-detection dataset collected from an enterprise-grade indoor 5G testbed, with radio, platform, and network KPIs under baseline and controlled anomalous operating conditions.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Network KPI |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Indoor, Office |
| Mobility | Not reported |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

The public dataset description does not expose one catalogue-wide carrier value.

## Supported wireless tasks

### [Network Anomaly Detection](../tasks/network-anomaly-detection.md)

**Inputs:** Network KPI

**Targets:** Anomaly label

**Scope:** Detect anomalous Open RAN operating periods from radio, platform, and network KPI streams.

**Task context:** Environment: Indoor, Office · Mobility: Not reported

Labels cover platform, fronthaul/network, radio, and mixed anomaly scenarios.

### [Network Fault Diagnosis](../tasks/network-fault-diagnosis.md)

**Inputs:** Network KPI

**Targets:** Anomaly label

**Scope:** Localize Open-RAN performance failures to the responsible KPI/component set after anomaly detection.

**Task context:** Environment: Indoor, Office · Mobility: Not reported

SpotLight explicitly includes an explainability/root-cause phase that identifies a minimal set of KPIs responsible for an anomaly; labels cover platform, network/fronthaul, radio, and mixed injected failures.

## Scale

- **Notes:** Traffic scenarios include 1/5 UEs running TCP, UDP, video, file download, ping, or HTTP, plus a 7-UE ping scenario.

## Resources

- [Dataset access](https://github.com/netsys-edinburgh/SpotLight)

## Caveats

- Anomalies are deliberately injected to mimic real operating failures and interference; the resource is therefore measured testbed data under controlled fault creation, not an observational field-failure corpus.

## References

- [SpotLight Dataset](https://github.com/netsys-edinburgh/SpotLight)
- [SpotLight: Accurate, Explainable and Efficient Anomaly Detection for Open RAN](https://doi.org/10.1145/3636534.3649380)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
