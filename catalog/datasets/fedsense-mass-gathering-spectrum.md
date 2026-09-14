<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# FedSENSE Mass-Gathering RF Spectrum Dataset

**Aliases:** A Real-World Multi-Band RF Dataset from a Mass-Gathering Event

A real multi-band RF spectrum-sensing dataset recorded during a large Montréal fireworks event, with 92,843 labeled frames across seven bands and raw I/Q for selected bands.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Spectrum, I/Q samples |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Outdoor, Urban |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Registration required |
| License | CC BY 4.0 |

## Frequency

**Regimes:** Sub-6 GHz

The acquisition sweeps 43 tiles across seven RF bands using a USRP B205mini-i.

## Supported wireless tasks

### [Spectrum Sensing](../tasks/spectrum-sensing.md)

**Inputs:** Spectrum, I/Q samples

**Targets:** Spectrum occupancy

**Scope:** Detect occupied versus unoccupied RF frames in real multi-band mass-gathering spectrum measurements.

**Task context:** Environment: Outdoor, Urban · Mobility: Not applicable · Frequency: Sub-6 GHz

The authors explicitly note that occupancy labels are energy-detector proxies, not protocol-verified truth.

## Scale

- **Samples:** 92,843
- **Duration (hours):** 0.85
- **Notes:** 51-minute event recording with 11.18% occupied-frame prior.

## Resources

- [Dataset access](https://doi.org/10.21227/F2RV-MS26)
- [Official homepage](https://github.com/atikmahabub42/FedSense)

## Caveats

- Labels are energy-detector proxies and the corpus covers one site, one evening and one receiver; the repository explicitly documents these limitations.

## References

- [FedSENSE](https://github.com/atikmahabub42/FedSense)
- [A Real-World Multi-Band RF Dataset from a Mass-Gathering Event for Spectrum Analysis Framework](https://doi.org/10.21227/F2RV-MS26)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
