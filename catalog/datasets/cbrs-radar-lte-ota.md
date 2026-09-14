<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Real-world Radar and LTE Signals in the CBRS Band

**Aliases:** Real-world Radar and LTE Signals Dataset Collected Over-the-air in Shared CBRS Band

A real over-the-air CBRS coexistence dataset containing LTE and radar signals under overlapping and non-overlapping conditions for machine-learning-based RF signal detection.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples |
| Technologies | LTE |
| Generation context | 4G, 5G |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 3.5 GHz CBRS band

The resource targets shared operation in the CBRS band.

## Supported wireless tasks

### [Signal Classification](../tasks/signal-classification.md)

**Inputs:** I/Q samples

**Targets:** Signal class

**Scope:** Detect/classify co-existing LTE and radar RF conditions from real over-the-air CBRS I/Q observations.

**Task context:** Environment: Laboratory · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Samples:** 5,640
- **Size (GB):** 55.5
- **Notes:** The official project page describes 5,640 40-ms samples with LTE/radar coexistence variations.

## Resources

- [Dataset access](https://genesys-lab.org/CBRS)

## Caveats

- The corpus is collected in controlled coexistence experiments and should not be treated as a complete field survey of CBRS activity.

## References

- [Real-world Radar and LTE Signals Dataset Collected Over-the-air in Shared CBRS Band](https://genesys-lab.org/CBRS)
- [Real-world Radar and LTE Signals Dataset Collected Over-the-air in Shared CBRS Band](https://doi.org/10.21227/ZDG0-7242)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
