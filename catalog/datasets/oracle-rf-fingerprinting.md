<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# ORACLE RF Fingerprinting Datasets

**Aliases:** ORACLE

A pair of RF-fingerprinting datasets built from USRP X310 transmitters, including over-the-air raw I/Q recordings and controlled over-the-cable IQ-imbalance recordings.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset family |
| Origin | Measurement |
| Modalities | I/Q samples |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Unknown |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 2.45 GHz

The over-the-air Wi-Fi recordings use a 2.45 GHz center frequency and 5 MS/s sampling rate.

## Supported wireless tasks

### [RF Fingerprinting](../tasks/rf-fingerprinting.md)

**Inputs:** I/Q samples

**Targets:** Device ID

**Scope:** Identify individual bit-similar USRP X310 transmitters from their physical-layer I/Q signatures.

**Task context:** Environment: Unknown · Mobility: Static · Frequency: Sub-6 GHz

## Scale

- **Devices:** 16
- **Notes:** The over-the-air dataset contains recordings from 16 bit-similar USRP X310 radios, with more than 20 million samples collected per radio.

## Resources

- [Dataset access](https://www.genesys-lab.org/oracle)

## Caveats

- The official ORACLE page releases both over-the-air raw-I/Q data and over-the-cable controlled-impairment data; experiments should state which subset is used because their channel conditions differ fundamentally.

## References

- [Datasets for RF Fingerprinting of Bit-similar USRP X310 Radios](https://www.genesys-lab.org/oracle)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
