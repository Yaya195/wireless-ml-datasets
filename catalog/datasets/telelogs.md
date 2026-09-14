<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# TeleLogs

**Aliases:** TeleLogs 5G Root Cause Analysis Benchmark

A synthetic 5G drive-test benchmark for root-cause analysis that combines user-plane KPIs, cell configuration parameters, mobility context, observed throughput degradation, and labels for eight network failure causes.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Synthetic |
| Modalities | Network KPI, Mobility trace |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Unknown |
| Mobility | Mobile |
| Temporal structure | Sequence |
| Access | Registration required |
| License | MIT |
| Collection(s) | [LLM & Foundation Model Resources](../collections/llm-foundation-model-resources.md) |

## Frequency

**Status:** Not Reported

A single catalogue-wide carrier configuration is not stated on the public dataset card.

## Supported wireless tasks

### [Network Fault Diagnosis](../tasks/network-fault-diagnosis.md)

**Inputs:** Network KPI, Mobility trace

**Targets:** Anomaly label

**Scope:** Diagnose the cause of 5G downlink throughput degradation from network configuration, mobility, and user-plane measurements.

**Task context:** Environment: Unknown · Mobility: Mobile

The benchmark explicitly defines eight labeled root causes including coverage, interference, mobility, handover, antenna, PCI, and resource-allocation failures.

## Scale

- **Size (GB):** 0.0148
- **Notes:** The benchmark defines eight root causes and provides training and test splits; the public card describes a gated dataset in the 1K–10K size category.

## Resources

- [Dataset access](https://huggingface.co/datasets/netop/TeleLogs)

## Caveats

- TeleLogs is a synthetic diagnostic benchmark rather than a field-failure corpus, and its gated access conditions ask users not to redistribute the benchmark publicly.

## References

- [TeleLogs — Hugging Face Dataset](https://huggingface.co/datasets/netop/TeleLogs)
- [Reasoning Language Models for Root Cause Analysis in 5G Wireless Networks](https://arxiv.org/abs/2507.21974)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
