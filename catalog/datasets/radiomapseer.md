<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RadioMapSeer

A public collection of simulated urban pathloss/RSS and time-of-arrival radio maps paired with city geometry and transmitter locations for radio-map learning and localization research.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Simulation |
| Modalities | Scene geometry, Radio map, Position, RSS |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Outdoor, Urban |
| Mobility | Not applicable |
| Temporal structure | Snapshot |
| Access | Open |
| License | CC BY 4.0 |

## Frequency

**Regimes:** Sub-6 GHz
**Bands:** 5.9 GHz

The original RadioMapSeer dataset uses a 5.9 GHz carrier with 10 MHz bandwidth.

## Supported wireless tasks

### [Radio Map Estimation](../tasks/radio-map-estimation.md)

**Inputs:** Scene geometry, Position

**Targets:** Radio map

**Scope:** Predict pathloss/RSS radio maps from urban map geometry and transmitter information.

**Task context:** Environment: Outdoor, Urban · Mobility: Not applicable · Frequency: Sub-6 GHz

### [Localization](../tasks/localization.md)

**Inputs:** RSS, Radio map

**Targets:** Position

**Scope:** RSS-based urban localization using user RSS measurements together with estimated pathloss radio maps as spatial reference.

**Task context:** Environment: Outdoor, Urban · Mobility: Not applicable · Frequency: Sub-6 GHz

The RSS measurement is the user observation; the radio maps provide the spatial propagation reference. The two are not interchangeable inputs.

## Scale

- **Samples:** 56,000
- **Scenarios:** 700
- **Size (GB):** 3.0
- **Notes:** The original RadioMapSeer release contains 700 urban maps with 80 transmitter locations per map (56,000 map-transmitter pairs).

## Resources

- [Dataset access](https://radiomapseer.github.io/)
- [Official repository](https://github.com/radiomapseer/radiomapseer.github.io)

## Caveats

- RadioMapSeer is simulation-based; results obtained on its generated urban maps should not be interpreted as direct validation on measured radio environments.

## References

- [RadioMapSeer Dataset](https://radiomapseer.github.io/)
- [Dataset of Pathloss and ToA Radio Maps With Localization Application](https://arxiv.org/abs/2212.11777)
- [Real-time Outdoor Localization Using Radio Maps: A Deep Learning Approach](https://arxiv.org/abs/2106.12556)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
