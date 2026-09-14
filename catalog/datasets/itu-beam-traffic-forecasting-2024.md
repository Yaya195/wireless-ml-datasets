<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# ITU Spatio-Temporal Beam-Level Traffic Forecasting Dataset

**Aliases:** Spatio-Temporal Beam-Level Traffic Forecasting Challenge Dataset

A beam-level cellular traffic time-series dataset released for the ITU 2024 forecasting challenge, containing hourly throughput volume, throughput time, PRB utilization, and user-count signals across gNodeBs, cells, and beams.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Unknown |
| Modalities | Traffic, Network KPI |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | Phased array |
| Environment | Unknown |
| Mobility | Unknown |
| Temporal structure | Sequence |
| Access | Registration required |
| License | CC BY-SA 4.0 |

## Frequency

**Status:** Not Reported

The forecasting resource is indexed by beam/cell/gNodeB rather than a documented catalogue-wide carrier.

## Supported wireless tasks

### [Traffic Prediction](../tasks/traffic-prediction.md)

**Inputs:** Traffic, Network KPI

**Targets:** Traffic volume

**Scope:** Forecast future hourly downlink throughput volume at beam level from historical throughput volume/time, PRB utilization, and user-count time series.

**Task context:** Environment: Unknown · Mobility: Unknown

The challenge predicts DLThpVol for both near-term and longer-horizon target weeks.

## Scale

- **Samples:** 2,419,200
- **Sites:** 30
- **Notes:** Training covers five weeks of hourly observations across 30 gNodeBs × 3 cells × 32 beams (2,880 beam series).

## Resources

- [Dataset access](https://zindi.africa/competitions/spatio-temporal-beam-level-traffic-forecasting-challenge)

## Caveats

- The challenge supplies five weeks of training data and asks for weeks 6 and 11; evaluation therefore includes a substantial long-horizon extrapolation gap.

## References

- [Spatio-Temporal Beam-Level Traffic Forecasting Challenge by ITU](https://zindi.africa/competitions/spatio-temporal-beam-level-traffic-forecasting-challenge)
- [The 5th edition of the ITU AI/ML in 5G Challenge: A year of competitions in review](https://aiforgood.itu.int/the-5th-edition-of-the-itu-ai-ml-in-5g-challenge-a-year-of-competitions-in-review/)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
