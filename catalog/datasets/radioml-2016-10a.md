<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RadioML 2016.10A

**Aliases:** RML2016.10A

A historical synthetic automatic-modulation-recognition dataset generated with GNU Radio, containing 11 analog/digital modulation classes under varying SNR.

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

The release contains complex-baseband synthetic waveforms rather than one RF carrier.

## Supported wireless tasks

### [Modulation Recognition](../tasks/modulation-recognition.md)

**Inputs:** I/Q samples

**Targets:** Modulation label

**Scope:** Classify one of 11 modulation classes from complex I/Q samples across varying SNR.

**Task context:** Environment: Not applicable · Mobility: Not applicable

## Scale

- **Samples:** 220,000
- **Notes:** 220,000 examples are commonly documented for the 11-class, variable-SNR release.

## Resources

- [Dataset access](https://opendata.deepsig.io/datasets/2016.10/RML2016.10a.tar.bz2)
- [Official repository](https://github.com/radioML/dataset)
- [Documentation](https://www.deepsig.ai/datasets/)

## Caveats

- DeepSig explicitly marks this as an old academic dataset with known errata and recommends newer real over-the-air data for new work.

## References

- [DeepSig Datasets](https://www.deepsig.ai/datasets/)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
