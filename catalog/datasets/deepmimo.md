<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# DeepMIMO

A public toolchain and database of site-specific wireless ray-tracing scenarios used to derive channel and propagation data for AI/ML research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Ray tracing |
| Modalities | Channel matrix, Path parameters, Position, Scene geometry |
| Technologies | 6G |
| Generation context | 6G |
| Radio configuration | Massive MIMO, MIMO |
| Environment | Indoor, Outdoor |
| Mobility | Configurable |
| Temporal structure | Configurable |
| Access | Open |
| License | Varies |

## Frequency

**Regimes:** mmWave, Sub-6 GHz, Sub-THz

Frequency coverage is scenario-dependent; the current database API exposes band filters.

## Supported wireless tasks

### [Beam Prediction](../tasks/beam-prediction.md)

**Inputs:** Channel matrix

**Targets:** Beam index

**Scope:** Scenario and configuration dependent; the original DeepMIMO work demonstrates a mmWave beam-prediction application.

**Task context:** Frequency: mmWave

### [Localization](../tasks/localization.md)

**Inputs:** Channel matrix

**Targets:** Position

**Scope:** Dynamic massive-MIMO localization from DeepMIMO-generated geo-tagged CSI/angle-delay representations.

**Task context:** Environment: Indoor, Outdoor · Mobility: Mobile · Frequency: mmWave

DyLoc explicitly uses DeepMIMO to generate geo-tagged CSI datasets for localization in indoor and outdoor dynamic scenarios.

### [Channel Estimation](../tasks/channel-estimation.md)

**Inputs:** Channel matrix

**Targets:** Channel

**Scope:** Evaluate learned wideband/beamspace massive-MIMO channel estimators using realistic DeepMIMO ray-traced channel realizations.

**Task context:** Environment: Outdoor · Mobility: Static · Frequency: mmWave

The cited study generates DeepMIMO channel realizations and derives beamspace measurements for channel-estimation evaluation.

### [Radio SLAM](../tasks/radio-slam.md)

**Inputs:** Path parameters, Scene geometry

**Targets:** Position, Scene / environment geometry

**Evaluation reference:** Position, Scene / environment geometry

**Scope:** Evaluate radio-geometric SLAM from ray-traced multipath delay/angle observations, receiver/transmitter positions, and interaction-point geometry generated from DeepMIMO scenarios.

**Task context:** Mobility: Configurable · Frequency: mmWave, Sub-THz

This mapping is based on documented DeepMIMO geometry plus maintainer-confirmed use in Radio-SLAM experiments; DeepMIMO is also broadly SLAM-capable because it exposes AoA/AoD, delays, interaction types/points, and scene geometry.

## Scale

- **Notes:** The current DeepMIMO database advertises 200+ scenarios and is growing.

## Resources

- [Dataset access](https://www.deepmimo.net/)
- [Official repository](https://github.com/DeepMIMO/DeepMIMO)
- [Documentation](https://www.deepmimo.net/docs/)
- [Loader / access tooling](https://www.deepmimo.net/docs/quickstart.html)

## Caveats

- DeepMIMO is a collection/toolchain rather than one fixed dataset; scenario and generation choices materially determine the resulting data.

## References

- [DeepMIMO unified repository](https://github.com/DeepMIMO/DeepMIMO)
- [DeepMIMO Database API](https://www.deepmimo.net/docs/api/database.html)
- [DeepMIMO: A Generic Deep Learning Dataset for Millimeter Wave and Massive MIMO Applications](https://arxiv.org/abs/1902.06435)
- [DyLoc: Dynamic Localization for Massive MIMO Using Predictive Recurrent Neural Networks](https://doi.org/10.1109/INFOCOM42981.2021.9488913)
- [Model-Data Hybrid-Driven Wideband Channel Estimation for Beamspace Massive MIMO Systems](https://doi.org/10.3390/e28020154)
- [UQAM seminar on AI-native wireless systems, localization, and Radio SLAM](https://evenements.uqam.ca/evenements/yaya-etiabi-ai-aided-and-ai-oriented-integrated-sensing-communication-and-computing/34058)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
