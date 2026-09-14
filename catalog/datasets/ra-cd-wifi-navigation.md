<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# RA-CD: Robot-Aided Wi-Fi Localization and Navigation Dataset

**Aliases:** Robot-Aided Collected Dataset, RA-CD

A real robot-collected Wi-Fi RSSI dataset from an obstacle-containing indoor grid, with labeled and unlabeled fingerprints used in a published hybrid-learning framework for both indoor localization and action-based navigation.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Wi-Fi RSSI, Position, Scene geometry |
| Technologies | Wi-Fi |
| Generation context | — |
| Radio configuration | — |
| Environment | Indoor |
| Mobility | Static |
| Temporal structure | Snapshot |
| Access | Open |
| License | Not Reported |

## Frequency

**Regimes:** Sub-6 GHz

The paper identifies Wi-Fi RSSI measurements but does not make a catalogue-level frequency band claim in the curated metadata.

## Supported wireless tasks

### [Localization](../tasks/localization.md)

**Inputs:** Wi-Fi RSSI

**Targets:** Position

**Scope:** Estimate the robot/grid location from measured Wi-Fi RSSI fingerprints.

**Task context:** Environment: Indoor · Mobility: Static · Frequency: Sub-6 GHz

### [Radio-Assisted Navigation](../tasks/radio-assisted-navigation.md)

**Inputs:** Wi-Fi RSSI, Position, Scene geometry

**Targets:** Navigation action / motion decision

**Scope:** Select motion actions in an obstacle-containing indoor grid using Wi-Fi-derived state/location information to guide the agent toward a target.

**Task context:** Environment: Indoor · Mobility: Mobile · Frequency: Sub-6 GHz

This is direct navigation evidence rather than a navigation-by-title inference: the paper trains and evaluates a distinct action model for the navigation task using RA-CD.

## Scale

- **Samples:** 7,920
- **Scenarios:** 1
- **Sites:** 1
- **Notes:** The paper reports 1,584 labeled fingerprints and 6,336 unlabeled fingerprints collected from seven Wi-Fi routers.

## Resources

- [Dataset access](https://github.com/MUST-AI-Lab/RA-HDL)
- [Documentation](https://www.mdpi.com/1424-8220/23/14/6320)

## Caveats

- The public files contain RSSI fingerprints and grid labels; navigation actions are learned within the paper’s MDP/action-model formulation rather than supplied as per-sample supervised action labels.

## References

- [RA-HDL — public data repository](https://github.com/MUST-AI-Lab/RA-HDL)
- [Wi-Fi-Based Indoor Localization and Navigation: A Robot-Aided Hybrid Deep Learning Approach](https://doi.org/10.3390/s23146320)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
