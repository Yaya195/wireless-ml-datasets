<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RF Jamming Dataset

**Aliases:** RF Jamming Dataset: A Wireless Spectral Scan Approach for Malicious Interference Detection

An experimentally measured wireless spectral-scan dataset and testbed release for machine-learning-based detection and characterization of malicious RF jamming/interference.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Spectrum |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | MIT License |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 2.4 GHz Wi-Fi band, 5 GHz Wi-Fi band

Published reuse descriptions identify the released WLAN spectral-scan data across the 2.4 and 5 GHz bands.

## Supported wireless tasks

### [Interference Classification](../tasks/interference-classification.md)

**Inputs:** Spectrum

**Targets:** Interference label

**Scope:** Detect or identify malicious RF jamming/interference conditions from measured spectral scans.

**Task context:** Environment: Laboratory · Mobility: Not applicable · Frequency: Sub-6 GHz

The associated work demonstrates ML-based jamming detection with experimentally measured data.

## Scale

- **Notes:** The public repository includes measured/preprocessed data, train/test splits, and reference models.

## Resources

- [Dataset access](https://github.com/abubakar-sani/CCA_classifiers)

## Caveats

- The dataset is collected under controlled jamming scenarios; deployment performance against previously unseen interferers, hardware, or ambient RF conditions requires separate evaluation.

## References

- [RF Jamming Dataset repository](https://github.com/abubakar-sani/CCA_classifiers)
- [RF Jamming Dataset: A Wireless Spectral Scan Approach for Malicious Interference Detection](https://doi.org/10.1109/MCOM.003.2300483)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
