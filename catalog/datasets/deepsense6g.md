<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# DeepSense 6G

**Aliases:** DeepSense6G

A large-scale real-world multimodal sensing and communication dataset organized into scenarios that combine wireless measurements with sensors such as camera, LiDAR, radar, and position.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset collection |
| Origin | Measurement |
| Modalities | Position, Camera, LiDAR, Radar, Beam power |
| Technologies | 6G |
| Generation context | 6G |
| Radio configuration | Phased array |
| Environment | Indoor, Outdoor, Urban, Parking lot, Vehicular |
| Mobility | Mixed |
| Temporal structure | Mixed |
| Access | Registration required |
| License | Not Reported |

## Frequency

**Status:** Varies

Frequency and hardware depend on scenario/task; several beam-related tasks use mmWave measurements.

## Supported wireless tasks

### [Beam Prediction](../tasks/beam-prediction.md)

**Inputs:** Position, Camera, LiDAR, Radar

**Targets:** Beam index

**Scope:** Task-specific scenario subsets; official variants include vision-, position-, LiDAR-, radar-, and multimodal-aided beam prediction.

**Task context:** Environment: Outdoor, Urban · Mobility: Mobile · Frequency: mmWave

Available input modality depends on the selected DeepSense6G task subset.

### [Blockage Prediction](../tasks/blockage-prediction.md)

**Inputs:** Radar, Beam power

**Targets:** Blockage status

**Scope:** Task-specific scenario subsets with sequential sensing or wireless observations and future blockage labels.

**Task context:** Environment: Outdoor, Urban · Mobility: Mobile · Frequency: mmWave

### [Beam Tracking](../tasks/beam-tracking.md)

**Inputs:** Position, Camera

**Targets:** Beam index

**Scope:** V2V beam-tracking development data using vehicle position and visual information in task-specific scenarios.

**Task context:** Environment: Outdoor, Vehicular · Mobility: Mobile · Frequency: mmWave

## Scale

- **Notes:** The project currently advertises 30+ scenarios collected at several locations.

## Resources

- [Dataset access](https://www.deepsense6g.net/)
- [Documentation](https://deepsense6g.net/ml-tasks)

## Caveats

- DeepSense6G is scenario- and task-oriented; modalities, frequencies, labels, and download requirements vary across subsets.

## References

- [DeepSense 6G](https://www.deepsense6g.net/)
- [DeepSense 6G ML Tasks](https://deepsense6g.net/ml-tasks)
- [Vision-Aided Beam Prediction](https://www.deepsense6g.net/vision-aided-beam-prediction/)
- [Radar-Aided Blockage Prediction](https://www.deepsense6g.net/radar-aided-blockage-prediction/)
- [V2V Beam Tracking Task](https://www.deepsense6g.net/v2v-beam-tracking-task/)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
