<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# spectrumHive IoT I/Q Dataset

A synthetic wireless I/Q dataset with 120,000 frames spanning QPSK, DBPSK, GFSK, QAM, LoRa CSS spreading factors, and noise, generated for AI-based spectrum sensing and modulation/signal classification research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Synthetic |
| Modalities | I/Q samples |
| Technologies | LoRaWAN |
| Generation context | — |
| Radio configuration | — |
| Environment | Not applicable |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Applicable

Complex-baseband frames are generated independently of one fixed RF carrier.

## Supported wireless tasks

### [Modulation Recognition](../tasks/modulation-recognition.md)

**Inputs:** I/Q samples

**Targets:** Modulation label

**Scope:** Recognize digital/LoRa modulation classes from complex I/Q frames across SNR variation.

**Task context:** Environment: Not applicable · Mobility: Not applicable

### [Signal Classification](../tasks/signal-classification.md)

**Inputs:** I/Q samples

**Targets:** Signal class

**Scope:** Classify wireless signal type versus noise and among multiple communication waveform classes.

**Task context:** Environment: Not applicable · Mobility: Not applicable

The dataset is explicitly released for AI-based spectrum-sensing applications and includes a noise class alongside 11 signal classes.

### [Spectrum Sensing](../tasks/spectrum-sensing.md)

**Inputs:** I/Q samples

**Targets:** Signal class

**Scope:** AI-based sensing of signal presence/type from complex I/Q frames spanning wireless waveforms and a noise class.

**Task context:** Environment: Not applicable · Mobility: Not applicable

The official release is explicitly described as a dataset for AI-based spectrum-sensing applications; it provides noise plus 11 waveform classes rather than a time-frequency occupancy mask.

## Scale

- **Samples:** 120,000
- **Notes:** 120,000 frames, 4,096 complex samples per frame, SNR from -5 to 30 dB.

## Resources

- [Dataset access](https://github.com/WirelessLabUSV/spectrumHiveDatasets/blob/main/spectrumHive_IoT_Dataset_IQstream.md)
- [Official homepage](https://github.com/WirelessLabUSV/spectrumHiveDatasets)

## Caveats

- The data are synthetic complex-baseband frames with modeled fading/clock offsets, not over-the-air captures.

## References

- [spectrumHive IoT Dataset IQstream](https://github.com/WirelessLabUSV/spectrumHiveDatasets/blob/main/spectrumHive_IoT_Dataset_IQstream.md)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
