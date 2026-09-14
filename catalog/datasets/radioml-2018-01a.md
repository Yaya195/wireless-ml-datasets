<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RadioML 2018.01A

**Aliases:** RADIOML 2018.01A

A historical DeepSig synthetic radio dataset containing complex I/Q examples across 24 digital and analog modulation types with simulated channel effects.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Synthetic |
| Modalities | I/Q samples |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Not applicable |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Registration required |
| License | CC BY-NC-SA 4.0 |

## Frequency

**Status:** Not Applicable

The public dataset is represented as complex baseband I/Q examples rather than a site-specific carrier-frequency dataset.

## Supported wireless tasks

### [Modulation Recognition](../tasks/modulation-recognition.md)

**Inputs:** I/Q samples

**Targets:** Modulation label

**Scope:** Classification of the modulation type from complex I/Q signal examples.

## Scale

- **Samples:** 2,000,000
- **Notes:** Each example contains 1,024 complex samples; 24 digital and analog modulation types are represented.

## Resources

- [Dataset access](https://opendata.deepsig.io/datasets/2018.01/2018.01.OSC.0001_1024x2M.h5.tar.gz)
- [Documentation](https://www.deepsig.ai/datasets/)

## Caveats

- DeepSig now labels these open datasets as historical, notes known errata, and does not recommend them as current supported data.

## References

- [DeepSig Datasets](https://www.deepsig.ai/datasets/)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
