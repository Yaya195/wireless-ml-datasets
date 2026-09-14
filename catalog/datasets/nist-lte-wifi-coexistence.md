<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# NIST LTE and Wi-Fi Coexistence Measurement Data

**Aliases:** LTE and Wi-Fi coexistence measurement data

A hardware measurement dataset with LTE and Wi-Fi coexistence experiments, including received complex I/Q samples, system metadata, SINR/power settings, and network performance KPIs.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples, Network KPI, Spectrum |
| Technologies | LTE, Wi-Fi |
| Generation context | 4G |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Open |
| License | NIST Open License |

## Frequency

**Regimes:** Sub-6 GHz

The experiments cover LTE/Wi-Fi coexistence in sub-6-GHz bands; consult the NIST README for exact setup-specific frequencies.

## Supported wireless tasks

### [Spectrum Sensing](../tasks/spectrum-sensing.md)

**Inputs:** I/Q samples

**Targets:** Spectrum occupancy

**Scope:** Use received baseband I/Q and experiment metadata to study occupancy/coexistence detection under LTE and Wi-Fi activity.

**Task context:** Environment: Laboratory · Mobility: Static · Frequency: Sub-6 GHz

The NIST metadata explicitly identifies spectrum sensing as a supported research use; occupancy labels are scenario-level rather than dense time-frequency masks.

### [Signal Classification](../tasks/signal-classification.md)

**Inputs:** I/Q samples

**Targets:** Signal class

**Scope:** Classify received RF observations according to the active LTE/Wi-Fi signal configuration.

**Task context:** Environment: Laboratory · Mobility: Static · Frequency: Sub-6 GHz

The NIST metadata explicitly lists signal classification as a supported research use.

## Scale

- **Scenarios:** 3
- **Notes:** The NIST description identifies three main coexistence cases: one LTE link, two LTE links, and one LTE plus one Wi-Fi link.

## Resources

- [Dataset access](https://catalog.data.gov/dataset/lte-and-wi-fi-coexistence-measurement-data)

## Caveats

- The dataset is a controlled coexistence measurement campaign with a small number of configured link cases; it should not be interpreted as a broad survey of arbitrary real-world LTE/Wi-Fi deployments.

## References

- [LTE and Wi-Fi coexistence measurement data](https://catalog.data.gov/dataset/lte-and-wi-fi-coexistence-measurement-data)
- [NIST LTE and Wi-Fi coexistence measurement data metadata](https://catalog.data.gov/dataset/lte-and-wi-fi-coexistence-measurement-data)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
