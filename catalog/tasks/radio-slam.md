<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Radio SLAM

Jointly estimate agent trajectory and radio-related map or landmark states from wireless measurements, optionally with auxiliary sensing.

**Aliases:** channel-SLAM, multipath-assisted SLAM

**Datasets in catalogue:** 3

| Dataset | Inputs | Targets | Evaluation reference | Temporal structure | Origin | Frequency | Environment | Mobility | Access |
|---|---|---|---|---|---|---|---|---|---|
| [DeepMIMO](../datasets/deepmimo.md)<br><sub>Collection</sub> | Path parameters, Scene geometry | Position, Scene / environment geometry | Position, Scene / environment geometry | Configurable | Ray tracing | mmWave, Sub-THz | Indoor, Outdoor | Configurable | Open |
| [Millimeter-Wave Radio SLAM: 60 GHz Indoor Sensing Dataset](../datasets/tampere-60ghz-radio-slam.md) | I/Q samples, Path parameters | Position, Scene / environment geometry | Position, Scene / environment geometry | Trajectory | Measurement | mmWave | Indoor, Campus | Mobile | Registration required |
| [P2SLAM Wi-Fi SLAM Dataset Collection](../datasets/p2slam-wifi-slam.md)<br><sub>Collection</sub> | Wi-Fi CSI, Odometry | Position, Orientation / heading, Scene / environment geometry | Position, Orientation / heading, Scene / environment geometry | Trajectory | Measurement | Sub-6 GHz | Indoor, Office | Mobile | Registration required |
