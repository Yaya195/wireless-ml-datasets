<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Occluded Indoor Target mmWave Tracking Dataset

**Aliases:** Tracking the Occluded Indoor Target with Scattered Millimeter Wave Signal

A mmWave FMCW sensing dataset containing raw beat-frequency signals and camera-derived target-position ground truth for locating and tracking humans under indoor non-line-of-sight occlusion.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Radar, Position |
| Technologies | — |
| Generation context | — |
| Radio configuration | Phased array |
| Environment | Indoor |
| Mobility | Not applicable |
| Temporal structure | Trajectory |
| Access | Registration required |
| License | CC BY 4.0 |

## Frequency

**Regimes:** mmWave

Collected with a TI IWR6843 FMCW mmWave radar platform.

## Supported wireless tasks

### [Device-Free Localization](../tasks/device-free-localization.md)

**Inputs:** Radar

**Targets:** Position

**Scope:** Estimate and track an occluded human target's indoor position from scattered mmWave FMCW signals.

**Task context:** Environment: Indoor · Mobility: Not applicable · Frequency: mmWave

## Scale

- **Notes:** Raw, intermediate and CNN-ready representations plus processing/training scripts are released.

## Resources

- [Dataset access](https://doi.org/10.21227/BCA8-3R93)
- [Official homepage](https://research.aalto.fi/en/datasets/tracking-the-occluded-indoor-target-with-scattered-millimeter-wav/)
- [Documentation](https://doi.org/10.1109/JSEN.2024.3447271)

## Caveats

- The camera is used to provide ground truth; the wireless inference input is the mmWave sensing signal.

## References

- [Tracking the Occluded Indoor Target with Scattered Millimeter Wave Signal](https://research.aalto.fi/en/datasets/tracking-the-occluded-indoor-target-with-scattered-millimeter-wav/)
- [Tracking the Occluded Indoor Target With Scattered Millimeter Wave Signal](https://doi.org/10.1109/JSEN.2024.3447271)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
