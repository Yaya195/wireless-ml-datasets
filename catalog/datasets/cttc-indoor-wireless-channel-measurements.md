<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# CTTC Indoor Wireless Channel Measurements

**Aliases:** Datasets of Indoor Wireless Channel Measurements for Machine Learning Applications

Measured raw-I/Q point-to-point indoor wireless channel data at 433 MHz, 708 MHz, and 2.45 GHz with QPSK/Gaussian excitation and several SNR conditions, released for machine-learning channel modeling and estimation research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples |
| Technologies | — |
| Generation context | — |
| Radio configuration | SISO |
| Environment | Indoor, Laboratory |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-GHz, Sub-6 GHz
**Bands:** 433 MHz, 708 MHz, 2.45 GHz

## Supported wireless tasks

### [Channel Estimation](../tasks/channel-estimation.md)

**Inputs:** I/Q samples

**Targets:** Channel

**Scope:** Develop/evaluate data-driven channel estimation and channel-model learning from measured transmitted/received I/Q sequences.

**Task context:** Environment: Indoor, Laboratory · Mobility: Static · Frequency: Sub-GHz, Sub-6 GHz

The dataset metadata explicitly lists Channel Estimation among its intended ML research uses.

## Scale

- **Size (GB):** 3.8
- **Notes:** Multiple frequency/SNR/waveform archives total approximately 3.8 GB.

## Resources

- [Dataset access](https://zenodo.org/records/4895133)
- [Official homepage](https://aristides.cttc.es/index.php/services)

## Caveats

- The measurements are static point-to-point laboratory channels rather than multi-user or mobile channel traces.

## References

- [Datasets of Indoor Wireless Channel Measurements for Machine Learning Applications](https://zenodo.org/records/4895133)
- [ARISTIDES Datasets](https://aristides.cttc.es/index.php/services)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
