<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Telecom Italia Milan Telecommunications Activity Dataset

**Aliases:** Milan Mobile Traffic Dataset, Telecommunications - SMS, Call, Internet - MI

A city-scale cellular-activity dataset released through the Telecom Italia Big Data Challenge, with 10-minute SMS, call, and Internet activity aggregates over a 100×100 grid covering Milan for roughly two months.

## Overview

| Field | Value |
|---|---|
| Resource type | Dataset |
| Origin | Measurement |
| Modalities | Traffic |
| Technologies | — |
| Generation context | — |
| Radio configuration | — |
| Environment | Urban |
| Mobility | Not applicable |
| Temporal structure | Sequence |
| Access | Open |
| License | Not Reported |

## Frequency

**Status:** Not Applicable

The resource contains spatial-temporal network activity aggregates, not PHY measurements.

## Supported wireless tasks

### [Traffic Prediction](../tasks/traffic-prediction.md)

**Inputs:** Traffic

**Targets:** Traffic volume

**Scope:** Forecast future grid-level cellular Internet/telecommunications activity from historical spatial-temporal traffic observations.

**Task context:** Environment: Urban · Mobility: Not applicable

The resource is a spatio-temporal cellular-traffic series; the catalogue records the prediction task rather than a particular forecasting model.

## Scale

- **Sequences:** 62
- **Sites:** 10,000
- **Notes:** Approximately 62 days at 10-minute resolution over a 100×100 spatial grid.

## Resources

- [Dataset access](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EGZHFV)
- [Documentation](https://doi.org/10.1038/sdata.2015.55)

## Caveats

- Traffic values are aggregated activity indices over geographic grid cells and time intervals, not per-user packet/flow traces.

## References

- [Telecommunications - SMS, Call, Internet - MI](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EGZHFV)
- [A multi-source dataset of urban life in the city of Milan and the Province of Trentino](https://doi.org/10.1038/sdata.2015.55)

## Metadata verification

**Status:** Verified

**Last checked:** `2026-09-14`
