<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RENEW Indoor Mobility Channel Measurement for Massive MIMO

Six measured indoor massive-MIMO channel datasets from a 64-antenna RENEW base station and seven clients, collected specifically to train/evaluate deep-RL user scheduling under LoS/NLoS and mobility.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Channel matrix |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | Massive MIMO |
| Environment | Indoor, Campus |
| Mobility | Mixed |
| Temporal structure | Sequence |
| Access | Open |
| License | RENEW Data Copyright and License Agreement |

## Frequency

**Regimes:** Sub-6 GHz

The uplink pilots use an 802.11 LTS OFDM structure; no single carrier is recorded here.

## Supported wireless tasks

### [User Scheduling](../tasks/user-scheduling.md)

**Inputs:** Channel matrix

**Targets:** —

**Scope:** Learn/evaluate massive-MIMO user scheduling policies from measured multi-user CSI under mobility and LoS/NLoS variation.

**Task context:** Environment: Indoor, Campus · Mobility: Mixed · Frequency: Sub-6 GHz

The official dataset page states that the data were collected to train a deep-RL user scheduler.

## Scale

- **Sequences:** 6
- **Devices:** 7
- **Size (GB):** 33.5
- **Notes:** Six LoS/NLoS mobility datasets total roughly 33.5 GB.

## Resources

- [Dataset access](https://renew-wireless.org/dataset-indoor-channel.html)
- [Official repository](https://github.com/renew-wireless/RENEWLab)

## Caveats

- One of the seven users is mobile while the remaining users are fixed; this structure should be preserved when interpreting mobility robustness.

## References

- [Indoor Mobility Channel Measurement for Massive MIMO](https://renew-wireless.org/dataset-indoor-channel.html)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
