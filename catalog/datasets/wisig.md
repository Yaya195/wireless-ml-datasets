<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# WiSig

**Aliases:** WiFi Signal Dataset

A large-scale Wi-Fi RF-fingerprinting dataset with 10 million packets from 174 off-the-shelf transmitters captured by 41 USRP receivers over four capture sessions spanning a month.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz

Wi-Fi captures are sub-6-GHz; the catalogue does not assign a single center frequency across the whole resource.

## Supported wireless tasks

### [RF Fingerprinting](../tasks/rf-fingerprinting.md)

**Inputs:** I/Q samples

**Targets:** Device ID

**Scope:** Identify Wi-Fi transmitters from RF fingerprints while studying receiver-, channel-, and day-induced domain shifts.

**Task context:** Environment: Laboratory · Mobility: Static · Frequency: Sub-6 GHz

## Scale

- **Samples:** 10,000,000
- **Devices:** 174
- **Size (GB):** 76.9
- **Notes:** Processed Full WiSig is approximately 76.9 GB; raw WiSig is much larger.

## Resources

- [Dataset access](https://cores.ee.ucla.edu/downloads/datasets/wisig/)
- [Official repository](https://github.com/WiSig-dataset)

## Caveats

- Receiver and capture-day changes materially affect fingerprinting performance; experimental splits should preserve those domain-shift factors.

## References

- [WiSig: RF Fingerprinting Dataset](https://cores.ee.ucla.edu/downloads/datasets/wisig/)
- [WiSig: A Large-Scale WiFi Signal Dataset for Receiver and Channel Agnostic RF Fingerprinting](https://doi.org/10.1109/ACCESS.2022.3154790)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
