<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# CONVERGE ICASSP 2026 Multimodal 6G Dataset

**Aliases:** CONVERGE Challenge Dataset

A real-world indoor multimodal dataset released for the ICASSP 2026 CONVERGE challenge, synchronizing RGB-D video with radio measurements for blockage prediction, UE localization, and future SRS channel prediction in a 6G-oriented mmWave testbed.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Camera, Channel matrix, Network KPI |
| Technologies | 5G NR, 6G |
| Generation context | 5G, 6G |
| Radio configuration | — |
| Environment | Indoor, Laboratory |
| Mobility | Configurable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** mmWave

The challenge uses a high-frequency indoor mmWave testbed with an FR2-capable gNB and UE; the released source does not state one catalogue-wide center frequency.

## Supported wireless tasks

### [Blockage Prediction](../tasks/blockage-prediction.md)

**Inputs:** Camera, Channel matrix

**Targets:** Blockage status

**Scope:** Predict future blockage state from synchronized visual and radio observations in the controlled indoor mmWave setup.

**Task context:** Environment: Indoor, Laboratory · Mobility: Configurable · Frequency: mmWave

The released annotations distinguish no, partial, and full blockage states.

### [Localization](../tasks/localization.md)

**Inputs:** Camera, Channel matrix

**Targets:** Position

**Scope:** Estimate UE position from the synchronized multimodal observations used in the challenge localization track.

**Task context:** Environment: Indoor, Laboratory · Mobility: Configurable · Frequency: mmWave

The released Task 2 annotations provide UE translation coordinates and the challenge evaluates localization with position RMSE.

### [Channel Prediction](../tasks/channel-prediction.md)

**Inputs:** Camera, Channel matrix

**Targets:** Channel

**Scope:** Predict future SRS channel measurements from synchronized visual and radio observations.

**Task context:** Environment: Indoor, Laboratory · Mobility: Configurable · Frequency: mmWave

The released challenge evaluates future SRS prediction; the originally advertised beam-prediction track is not mapped because it is not part of the released v1 task set/results.

## Scale

- **Sites:** 1
- **Size (GB):** 4.8
- **Notes:** Zenodo v1 distributes training and validation archives totaling approximately 4.8 GB.

## Resources

- [Dataset access](https://zenodo.org/records/20849945)
- [Official homepage](https://converge-project.eu/converge-icassp-2026-sp-grand-challenge/)

## Caveats

- The official challenge page originally listed a beam-prediction track, but the released Zenodo v1 dataset and final ICASSP 2026 challenge results document three tasks only; beam prediction is therefore not mapped here.

## References

- [CONVERGE Challenge Dataset: Multimodal Sensing for 6G Wireless Communications (ICASSP 2026)](https://zenodo.org/records/20849945)
- [CONVERGE Challenge: Multimodal Learning for 6G Wireless Communications](https://converge-project.eu/converge-icassp-2026-sp-grand-challenge/)
- [CONVERGE Challenge: Multimodal Learning for 6G Wireless Communications](https://www.eurecom.fr/publication/8684)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`

Verified against the Zenodo dataset record, official CONVERGE challenge page, and ICASSP 2026 challenge paper.
