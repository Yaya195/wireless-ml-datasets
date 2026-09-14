<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# LoRa Sensor RF Fingerprinting Dataset

**Aliases:** LoRa sensor data sets for RF finger printing via Self-Organizing Feature Maps

A public RF-fingerprinting dataset of LoRa sensor transmissions, including raw I/Q data and derived self-organizing-feature-map representations for device authentication.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Open |
| License | Non-Commercial Government Licence for public sector information |

## Frequency

**Regimes:** Sub-GHz

The dataset concerns LoRa sensor links; exact collection carrier is left to the release documentation.

## Supported wireless tasks

### [RF Fingerprinting](../tasks/rf-fingerprinting.md)

**Inputs:** I/Q samples

**Targets:** Device ID

**Scope:** Identify/authenticate LoRa sensor devices from device-specific RF fingerprints.

**Task context:** Environment: Laboratory · Mobility: Static · Frequency: Sub-GHz

## Scale

- **Devices:** 6
- **Size (GB):** 0.064
- **Notes:** The Bristol mirror contains raw LoRa I/Q data plus derived SOFM images for six transmitters.

## Resources

- [Dataset access](https://data.bris.ac.uk/data/dataset/3u4rzcddg047028q6snonqtnd9)
- [Official homepage](https://research-information.bris.ac.uk/en/datasets/lora-sensor-data-sets-for-rf-finger-printing-via-self-organizing-/)
- [Documentation](https://research-information.bris.ac.uk/en/publications/iot-device-authentication-using-self-organizing-feature-map-data-/)

## Caveats

- The public mirror includes both raw I/Q and post-processed SOFM representations; experiments should state which representation is used.

## References

- [LoRa sensor data sets for RF finger printing via Self-Organizing Feature Maps](https://research-information.bris.ac.uk/en/datasets/lora-sensor-data-sets-for-rf-finger-printing-via-self-organizing-/)
- [Nair et al. IoT Device Authentication CommsMag dataset](https://data.bris.ac.uk/data/dataset/3u4rzcddg047028q6snonqtnd9)
- [IoT Device Authentication Using Self-Organizing Feature Map Data Sets](https://doi.org/10.1109/MCOM.002.2200705)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
