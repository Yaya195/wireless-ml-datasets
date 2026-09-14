<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# DeepSense Spectrum-Sensing Datasets

A two-part spectrum-sensing collection containing real over-the-air IEEE 802.11 a/g I/Q captures and simulated LTE-M uplink I/Q data with occupancy labels for wideband sensing.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Hybrid |
| Modalities | I/Q samples, Spectrum |
| Technologies | Wi-Fi, LTE |
| Generation context | — |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | MIT |

## Frequency

**Regimes:** Sub-6 GHz

The real Wi-Fi collection spans four 5-MHz subchannels over a 20-MHz observation bandwidth; LTE-M is simulated over 10 MHz.

## Supported wireless tasks

### [Spectrum Sensing](../tasks/spectrum-sensing.md)

**Inputs:** I/Q samples

**Targets:** Spectrum occupancy

**Scope:** Infer occupied sub-bands from wideband I/Q observations in Wi-Fi and LTE-M experiments.

**Task context:** Environment: Laboratory · Mobility: Not applicable · Frequency: Sub-6 GHz

## Resources

- [Dataset access](https://github.com/wineslab/deepsense-spectrum-sensing-datasets)

## References

- [DeepSense spectrum sensing datasets](https://github.com/wineslab/deepsense-spectrum-sensing-datasets)
- [DeepSense: Fast Wideband Spectrum Sensing Through Real-Time In-the-Loop Deep Learning](https://doi.org/10.1109/INFOCOM42981.2021.9488764)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
