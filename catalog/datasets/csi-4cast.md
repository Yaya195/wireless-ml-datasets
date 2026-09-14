<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# CSI-4CAST

**Aliases:** CSI-4CAST Channel State Information Forecasting Dataset

A large collection of pre-generated 3GPP TR 38.901 CSI forecasting datasets covering CDL-A–E models, delay spreads, user speeds, TDD/FDD settings, and regular/generalization evaluation regimes.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Simulation |
| Modalities | Channel matrix |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | MIMO |
| Environment | Unknown |
| Mobility | Configurable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

Frequency configuration is experiment-dependent across FDD/TDD datasets.

## Supported wireless tasks

### [Channel Prediction](../tasks/channel-prediction.md)

**Inputs:** Channel matrix

**Targets:** Channel

**Scope:** Forecast future uplink/downlink CSI from historical CSI across channel models, delay spreads, speeds, and generalization conditions.

**Task context:** Environment: Unknown · Mobility: Configurable

## Scale

- **Scenarios:** 565
- **Notes:** The Hugging Face organization exposes hundreds of train/test/generalization dataset repositories.

## Resources

- [Dataset access](https://huggingface.co/CSI-4CAST)
- [Official repository](https://github.com/AI4OPT/CSI-4CAST)
- [Documentation](https://github.com/AI4OPT/CSI-4CAST/blob/main/z_artifacts/data/info.md)

## Caveats

- CSI-4CAST is a large generated collection split into many repositories; comparisons must report the exact channel model, delay spread, speed, duplex setting, and regular/generalization split.

## References

- [CSI-4CAST Organization](https://huggingface.co/CSI-4CAST)
- [CSI-4CAST](https://github.com/AI4OPT/CSI-4CAST)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
