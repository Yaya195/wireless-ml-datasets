<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# GENESYS Channel-Resilient RF Fingerprinting Datasets

**Aliases:** Data Augmentation RF Fingerprinting Dataset

Three simulated RF-fingerprinting datasets (TxData, Day1, Day2) built from virtual 802.11a radios with controlled I/Q imbalance and channel/SNR variation for channel-resilient fingerprinting research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset family |
| Origin | Simulation |
| Modalities | I/Q samples |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Not applicable |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz

802.11a waveform generation is used; no single center frequency is assigned in the catalogue.

## Supported wireless tasks

### [RF Fingerprinting](../tasks/rf-fingerprinting.md)

**Inputs:** I/Q samples

**Targets:** Device ID

**Scope:** Identify virtual radios from hardware-impairment fingerprints under controlled channel and SNR shifts.

**Task context:** Environment: Not applicable · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Devices:** 10
- **Size (GB):** 92.0
- **Notes:** TxData is ~2 GB; Day1 and Day2 are ~45 GB each.

## Resources

- [Dataset access](https://genesys-lab.org/dataaugmentation)

## Caveats

- These are MATLAB-simulated virtual-radio fingerprints rather than captures from physical transmitters.

## References

- [MATLAB Simulated Datasets for Channel-Resilient RF Fingerprinting](https://genesys-lab.org/dataaugmentation)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
