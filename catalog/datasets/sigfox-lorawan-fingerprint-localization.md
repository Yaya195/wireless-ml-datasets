<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Sigfox and LoRaWAN Datasets for Fingerprint Localization in Large Urban and Rural Areas

**Aliases:** Sigfox and LoRaWAN fingerprint localization datasets

A measured LPWAN collection with Sigfox and LoRaWAN gateway RSSI plus GPS-labelled uplink messages for fingerprint localization in large urban and rural areas.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | RSS, SNR / signal-quality measurements, Position |
| Technologies | LoRaWAN, Sigfox |
| Generation context | — |
| Radio configuration | — |
| Environment | Outdoor, Urban, Rural |
| Mobility | Mobile |
| Temporal structure | Sequence |
| Access | Open |
| License | CC BY 4.0 |

## Frequency

**Status:** Not Reported

The release identifies the LPWAN technologies but does not provide one collection-wide carrier specification.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** RSS

**Targets:** Position

**Scope:** Estimate outdoor device position from LPWAN gateway RSSI fingerprints and associated network measurements.

**Task context:** Environment: Outdoor, Urban, Rural · Mobility: Mobile

Version 1.3 also exposes timing metadata for the LoRaWAN subset, but no additional task mapping is inferred from availability alone.

## Scale

- **Samples:** 170,446
- **Scenarios:** 3
- **Notes:** Version 1.3 contains 130,430 LoRaWAN urban messages, 14,378 Sigfox urban messages, and 25,638 Sigfox rural messages.

## Resources

- [Dataset access](https://zenodo.org/records/3904158)
- [Documentation](https://doi.org/10.3390/data3020013)

## Caveats

- Version 1.3 updates only the LoRaWAN subset; the two Sigfox subsets remain unchanged from earlier releases.

## References

- [Sigfox and LoRaWAN Datasets for Fingerprint Localization in Large Urban and Rural Areas](https://zenodo.org/records/3904158)
- [Sigfox and LoRaWAN Datasets for Fingerprint Localization in Large Urban and Rural Areas](https://doi.org/10.3390/data3020013)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-10-20`
