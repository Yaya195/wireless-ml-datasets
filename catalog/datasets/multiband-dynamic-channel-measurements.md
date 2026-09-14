<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Multi-Band Dynamic Channel Prediction Dataset

**Aliases:** Multi-Band Measurements for Deep Learning-Based Dynamic Channel Prediction and Simulation

A measured multi-band wireless-channel dataset collected with a dedicated testbed at sub-6-GHz and mmWave frequencies for dynamic channel prediction and learned channel simulation.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Channel impulse response, Channel matrix |
| Technologies | — |
| Generation context | 5G |
| Radio configuration | — |
| Environment | Industrial, Unknown |
| Mobility | Mobile |
| Temporal structure | Sequence |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz, mmWave

The paper explicitly describes measurements at sub-6-GHz and mmWave bands.

## Supported wireless tasks

### [Channel Prediction](../tasks/channel-prediction.md)

**Inputs:** Channel impulse response, Channel matrix

**Targets:** Channel

**Scope:** Forecast future dynamic channel impulse responses from measured multi-band channel histories.

**Task context:** Environment: Industrial, Unknown · Mobility: Mobile · Frequency: Sub-6 GHz, mmWave

## Scale

- **Notes:** The public dataset supports channel impulse-response forecasting and synthetic channel generation.

## Resources

- [Dataset access](https://doi.org/10.21227/3TPP-J394)
- [Documentation](https://re.public.polimi.it/handle/11311/1255397)

## Caveats

- The same resource also supports learned channel simulation; that is not represented as a separate wireless task in the current ontology.

## References

- [Multi-Band Measurements for Deep Learning-Based Dynamic Channel Prediction and Simulation](https://doi.org/10.21227/3TPP-J394)
- [Multi-Band Measurements for Deep Learning-Based Dynamic Channel Prediction and Simulation](https://doi.org/10.1109/MCOM.003.2200718)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
