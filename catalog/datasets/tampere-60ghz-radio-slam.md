<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Millimeter-Wave Radio SLAM: 60 GHz Indoor Sensing Dataset

**Aliases:** Tampere 60 GHz Radio SLAM Dataset

A measured 60 GHz indoor bistatic sensing dataset based on 5G NR positioning reference signals, providing raw I/Q data, estimated multipath parameters, receiver trajectory information, and an environment map for radio positioning and SLAM.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples, Path parameters, Position, Scene geometry |
| Technologies | 5G NR, 6G |
| Generation context | 5G, 6G |
| Radio configuration | Phased array |
| Environment | Indoor, Campus |
| Mobility | Mobile |
| Temporal structure | Trajectory |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Regimes:** mmWave
**Bands:** 60 GHz

The measurement campaign operates at 60 GHz.

## Supported wireless tasks

### [Radio SLAM](../tasks/radio-slam.md)

**Inputs:** I/Q samples, Path parameters

**Targets:** Position, Scene / environment geometry

**Evaluation reference:** Position, Scene / environment geometry

**Scope:** Jointly recover receiver state and multipath/environment landmarks from raw I/Q or estimated radio-path parameters in a measured indoor mmWave environment.

**Task context:** Environment: Indoor, Campus · Mobility: Mobile · Frequency: mmWave

The dataset additionally provides an environment map for evaluating mapping outputs; position is recorded as an evaluation reference rather than redefining SLAM as coordinate regression.

### [Localization](../tasks/localization.md)

**Inputs:** I/Q samples, Path parameters

**Targets:** Position

**Scope:** Estimate receiver position from 60 GHz PRS measurements and/or estimated multipath parameters.

**Task context:** Environment: Indoor, Campus · Mobility: Mobile · Frequency: mmWave

## Scale

- **Sites:** 1
- **Size (GB):** 128.8
- **Notes:** Six raw-I/Q archives total approximately 128.8 GB, excluding small postprocessed/support files.

## Resources

- [Dataset access](https://ieee-dataport.org/open-access/millimeter-wave-radio-slam-60-ghz-indoor-sensing-dataset)
- [Official homepage](https://research.tuni.fi/wireless/news/millimeter-wave-radio-slam-60-ghz-indoor-sensing-dataset/)
- [Documentation](https://researchportal.tuni.fi/en/datasets/millimeter-wave-radio-slam-60-ghz-indoor-sensing-dataset/)

## Caveats

- The measurement campaign is a single indoor 60 GHz environment with a specific trajectory and hardware setup; generalization to other sites and radio front ends must be evaluated separately.

## References

- [Millimeter-Wave Radio SLAM: 60 GHz Indoor Sensing Dataset](https://researchportal.tuni.fi/en/datasets/millimeter-wave-radio-slam-60-ghz-indoor-sensing-dataset/)
- [Tampere Wireless Research Center dataset announcement](https://research.tuni.fi/wireless/news/millimeter-wave-radio-slam-60-ghz-indoor-sensing-dataset/)
- [Millimeter-Wave Radio SLAM: End-to-End Processing Methods and Experimental Validation](https://doi.org/10.1109/JSAC.2024.3413995)
- [Millimeter-Wave Radio SLAM: 60 GHz Indoor Sensing Dataset](https://ieee-dataport.org/open-access/millimeter-wave-radio-slam-60-ghz-indoor-sensing-dataset)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
