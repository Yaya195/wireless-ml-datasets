<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# WiFiSpectralJam

**Aliases:** WiFiSpectralJam RF Jamming Dataset

A large commodity-Wi-Fi spectral-scan dataset with benign background, RF-chamber floor, and controlled jamming captures across active/passive scanning in the 2.4 and 5 GHz bands.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Spectrum |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Laboratory, Unknown |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 2.4 GHz Wi-Fi band, 5 GHz Wi-Fi band

## Supported wireless tasks

### [Interference Classification](../tasks/interference-classification.md)

**Inputs:** Spectrum

**Targets:** Interference label

**Scope:** Detect and characterize controlled RF-jamming/interference conditions from commodity-NIC spectral scans.

**Task context:** Environment: Laboratory, Unknown · Mobility: Not applicable · Frequency: Sub-6 GHz

## Scale

- **Samples:** 522,771,130
- **Size (GB):** 14.52
- **Notes:** The release contains 96,090 CSV files and over 522 million ordered spectral observations.

## Resources

- [Dataset access](https://www.kaggle.com/datasets/daniaherzalla/radio-frequency-jamming/data)
- [Documentation](https://arxiv.org/abs/2608.15728)

## Caveats

- Jamming is deliberately injected under controlled conditions; unseen jammer hardware and ambient RF domains remain separate generalization questions.

## References

- [WiFiSpectralJam: A Large-Scale Open Wi-Fi Spectral Scan Dataset with Controlled RF Jamming](https://arxiv.org/abs/2608.15728)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
