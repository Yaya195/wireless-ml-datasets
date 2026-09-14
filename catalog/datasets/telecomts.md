<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# TelecomTS

**Aliases:** TelecomTS Multi-Modal Observability Dataset

A large-scale multi-modal 5G observability dataset combining network KPI time series with natural-language descriptions, labels, anomaly metadata, troubleshooting context, and millions of question-answer instances for time-series and language reasoning.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Hybrid |
| Modalities | Network KPI, Text / natural language |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | MIT |
| Collection(s) | [LLM & Foundation Model Resources](../collections/llm-foundation-model-resources.md) |

## Frequency

**Status:** Not Reported

The public dataset description does not define one catalogue-wide carrier frequency.

## Supported wireless tasks

### [Network Anomaly Detection](../tasks/network-anomaly-detection.md)

**Inputs:** Network KPI

**Targets:** Anomaly label

**Scope:** Detect anomalous operating periods from multi-layer 5G KPI time series and contextual observability data.

**Task context:** Environment: Laboratory · Mobility: Mixed

The dataset explicitly supports binary anomaly detection and anomaly-duration localization.

### [Network Fault Diagnosis](../tasks/network-fault-diagnosis.md)

**Inputs:** Network KPI, Text / natural language

**Targets:** Anomaly label

**Scope:** Identify the root cause of 5G network anomalies from KPI time series, contextual metadata, and troubleshooting information.

**Task context:** Environment: Laboratory · Mobility: Mixed

Root-cause analysis is an explicit multi-class downstream task; natural-language Q&A also supports multimodal diagnostic reasoning.

## Scale

- **Samples:** 32,000
- **Size (GB):** 1.27
- **Notes:** The official repository reports about 32,000 time-series samples, 18 channels, 11 anomaly types, and 2,210,185 Q&A instances.

## Resources

- [Dataset access](https://huggingface.co/datasets/AliMaatouk/TelecomTS)
- [Official repository](https://github.com/Ali-maatouk/TelecomTS)

## Caveats

- The phrase "anomaly duration localization" refers to temporal sequence labeling of an anomaly interval, not spatial wireless localization; do not map this record to the localization task on that basis.
- The application label is contextual metadata used in descriptions and Q&A; it is not by itself evidence of a demonstrated traffic-classification benchmark, so no traffic-classification mapping is asserted.
- The anomaly corpus mixes synthetic fault types with one real over-the-air jamming anomaly, so results should distinguish controlled anomaly generation from naturally occurring field failures.

## References

- [TelecomTS — Official Repository](https://github.com/Ali-maatouk/TelecomTS)
- [TelecomTS — Hugging Face Dataset](https://huggingface.co/datasets/AliMaatouk/TelecomTS)
- [TelecomTS: A Multi-Modal Observability Dataset for Time Series and Language Analysis](https://arxiv.org/abs/2510.06063)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
