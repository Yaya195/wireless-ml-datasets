<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# HisarMod2019.1

**Aliases:** HisarMod

A synthetic automatic-modulation-recognition dataset with 26 modulation classes under ideal, static, Rayleigh, Rician, and Nakagami-m channels and a broad SNR range.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Synthetic |
| Modalities | I/Q samples |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Not applicable |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Status:** Not Applicable

Synthetic complex-baseband signals are not tied to one RF carrier.

## Supported wireless tasks

### [Modulation Recognition](../tasks/modulation-recognition.md)

**Inputs:** I/Q samples

**Targets:** Modulation label

**Scope:** Classify 26 modulation classes across multiple fading models and SNR conditions.

**Task context:** Environment: Not applicable · Mobility: Not applicable

## Scale

- **Samples:** 780,000
- **Size (GB):** 5.13
- **Notes:** Published descriptions report 780,000 signals, each with 1,024 I/Q samples.

## Resources

- [Dataset access](https://ieee-dataport.org/open-access/hisarmod-new-challenging-modulated-signals-dataset)
- [Documentation](https://arxiv.org/abs/1911.04970)

## Caveats

- The resource is fully synthetic; its fading diversity does not substitute for over-the-air domain validation.

## References

- [HisarMod: A New Challenging Modulated Signals Dataset](https://ieee-dataport.org/open-access/hisarmod-new-challenging-modulated-signals-dataset)
- [Robust and Fast Automatic Modulation Classification with CNN under Multipath Fading Channels](https://arxiv.org/abs/1911.04970)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
