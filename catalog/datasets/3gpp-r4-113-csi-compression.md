<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# 3GPP R4-113 NR AI/ML CSI Compression Datasets

**Aliases:** 3GPP R4-113 CSI Compression Datasets

Official 3GPP RAN4 shared NR AI/ML CSI-compression datasets contributed by Nokia, OPPO, and CAT/CATT for learned CSI compression and reconstruction studies.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Unknown |
| Modalities | Channel matrix |
| Technologies | 5G NR |
| Generation context | 5G |
| Radio configuration | Massive MIMO |
| Environment | Unknown |
| Mobility | Unknown |
| Temporal structure | Unknown |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Reported

No single verified carrier/band is assigned at collection level.

## Supported wireless tasks

### [CSI Feedback](../tasks/csi-feedback.md)

**Inputs:** Channel matrix

**Targets:** Channel

**Scope:** Train and evaluate learned CSI compression/reconstruction methods for NR channel-state feedback.

**Task context:** Environment: Unknown · Mobility: Unknown

## Scale

- **Samples:** 1,300,000
- **Scenarios:** 3
- **Notes:** Publicly documented files contain approximately 600k Nokia, 600k OPPO, and 100k CAT/CATT CSI samples.

## Resources

- [Dataset access](https://www.3gpp.org/ftp/tsg_ran/WG4_Radio/Data_sharing/NR_AIML_air/CSI_compression/Datasets/R4_113)

## Caveats

- The three vendor-contributed datasets should not be assumed to share identical propagation, generation, or domain characteristics; cross-vendor evaluation is itself a distribution-shift question.

## References

- [3GPP NR AI/ML Air Interface CSI Compression Datasets (R4-113)](https://www.3gpp.org/ftp/tsg_ran/WG4_Radio/Data_sharing/NR_AIML_air/CSI_compression/Datasets/R4_113)
- [CPC-based neural CSI compression using the official 3GPP R4-113 datasets](https://github.com/AhmedRadwan02/cpc-3gpp)
- [Contrastive Predictive Coding with Compression for Enhanced Channel State Feedback in Wireless Networks](https://arxiv.org/abs/2607.05419)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
