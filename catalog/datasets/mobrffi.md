<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# MobRFFI

**Aliases:** MobRFFI: A WiFi RF Fingerprinting Dataset with Granular Multi-Receiver Signal Capture

A multi-receiver Wi-Fi RF-fingerprinting dataset collected on the ORBIT testbed across separate days for device fingerprinting and re-identification under receiver and temporal variation.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | I/Q samples |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Laboratory |
| Mobility | Static |
| Temporal structure | Sequence |
| Access | Restricted |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 2.462 GHz Wi-Fi channel 11

The associated work documents 25 Msps captures on Wi-Fi channel 11.

## Supported wireless tasks

### [RF Fingerprinting](../tasks/rf-fingerprinting.md)

**Inputs:** I/Q samples

**Targets:** Device ID

**Scope:** Fingerprint and re-identify Wi-Fi emitters across multiple receivers and collection days.

**Task context:** Environment: Laboratory · Mobility: Static · Frequency: Sub-6 GHz

## Scale

- **Notes:** The release spans multiple simultaneous receivers and separate collection days; a reduced onboarding subset is also provided.

## Resources

- [Dataset access](https://doi.org/10.21227/XYAV-RH42)
- [Official homepage](https://arxiv.org/abs/2503.02156)

## Caveats

- The full DataPort artifact is large and non-open, which may limit accessibility despite the public paper and tooling.

## References

- [MobRFFI: A WiFi RF Fingerprinting Dataset with Granular Multi-Receiver Signal Capture](https://doi.org/10.21227/XYAV-RH42)
- [MobRFFI: Non-cooperative Device Re-identification for Mobility Intelligence](https://arxiv.org/abs/2503.02156)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
