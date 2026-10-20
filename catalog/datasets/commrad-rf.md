<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# CommRad RF

**Aliases:** CommRad RF communication radio dataset

A measured baseband RF dataset containing communication-radio signals from 27 handheld radios, collected for RF fingerprinting, identification, and classification.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-GHz
**Bands:** 136-174 MHz

The data article reports 136-174 MHz, 25 kHz channel bandwidth, and a 50 kS/s I/Q rate.

## Supported wireless tasks

### [RF Fingerprinting](../tasks/rf-fingerprinting.md)

**Inputs:** I/Q samples

**Targets:** Device ID

**Scope:** Identify communication-radio emitters from device-specific baseband I/Q signal fingerprints.

**Task context:** Environment: Indoor · Mobility: Not applicable · Frequency: Sub-GHz

The dataset article explicitly positions the recordings for RF fingerprinting and emitter identification.

## Scale

- **Devices:** 27
- **Size (GB):** 2.0
- **Notes:** The release contains more than 2,700 recorded RF signals from 27 radios.

## Resources

- [Dataset access](https://zenodo.org/records/14192970)
- [Documentation](https://doi.org/10.1016/j.dib.2025.111387)

## References

- [CommRad RF: A dataset of communication radio signals for detection, identification and classification](https://zenodo.org/records/14192970)
- [CommRad RF: A dataset of communication radio signals for detection, identification and classification](https://doi.org/10.1016/j.dib.2025.111387)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-10-20`
