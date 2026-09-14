<!-- GENERATED FILE — DO NOT EDIT DIRECTLY -->

# Supporting benchmarks & discovery resources

These resources complement the task-mapped dataset catalogue. They are curated to help users run established benchmarks or continue a personalized dataset search; they are not included in the core dataset count.

Supporting resources: **19**

## Cross-cutting collections

- [LLM & Foundation Model Resources](collections/llm-foundation-model-resources.md) — Telecom- and wireless-specific datasets, evaluation benchmarks, and suites for large language models and foundation models.

## Benchmark datasets, suites & frameworks

| Resource | Type | Focus | Access | How to use |
|---|---|---|---|---|
| [6G-Bench](https://github.com/maferrag/6G-Bench) | Benchmark dataset | Wireless Specific | Open | Use for foundation-model reasoning over AI-native 6G concepts; the project also distributes the validated benchmark data. |
| [GSMA Open Telco Evaluations](https://github.com/gsma-labs/evals) | Benchmark suite | Telecom Specific | Open | Use as a runnable benchmark suite when comparing telecom LLMs consistently across multiple public evaluations. |
| [IPIN Indoor Localization Competitions](https://www.ipin-conference.org/resources.html) | Benchmark platform | Wireless Specific | Open | Use the competition resources page to choose a year and sensing track matching your localization setting; several released datasets are archived on stable repositories such as Zenodo. |
| [ORANBench](https://huggingface.co/datasets/prnshv/ORANBench) | Benchmark dataset | Telecom Specific | Open | Use for O-RAN specification reasoning; the full ORAN-Bench-13K source benchmark is linked from the dataset card. |
| [PIRL-WIN](https://github.com/Panshark/PIRL-WIN) | Benchmark framework | Wireless Specific | Open | Use when you need an executable radio-assisted-navigation benchmark/framework with wireless digital-twin simulation and navigation-policy evaluation rather than a standalone measured dataset. |
| [SenseFi](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark) | Benchmark framework | Wireless Specific | Open | Use when you want a reproducible Wi-Fi CSI sensing benchmark pipeline rather than another dataset list. |
| [srsRANBench](https://huggingface.co/datasets/prnshv/srsRANBench) | Benchmark dataset | Telecom Specific | Open | Use for telecom software/code reasoning around an open-source 5G RAN implementation. |
| [TeleMath](https://huggingface.co/datasets/netop/TeleMath) | Benchmark dataset | Telecom Specific | Open | Use for telecom mathematical reasoning; it is a model-evaluation benchmark, not a raw wireless measurement dataset. |
| [TeleQnA](https://github.com/netop-team/TeleQnA) | Benchmark dataset | Telecom Specific | Open | Use when evaluating telecom-domain factual and conceptual knowledge rather than a specific wireless engineering task. |
| [TeleTables](https://huggingface.co/datasets/netop/TeleTables) | Benchmark dataset | Telecom Specific | Open | Use for standards-grounded table interpretation and multimodal telecom reasoning. |
| [TorchSig](https://github.com/TorchDSP/torchsig) | Benchmark framework | Wireless Specific | Open | Use to generate reproducible RFML datasets and baselines; current releases replace the legacy fixed Sig53/WidebandSig53 naming with configurable Narrowband/Wideband datasets. |
| [WirelessBench](https://wirelessbench.github.io/) | Benchmark dataset | Wireless Specific | Open | Use for wireless-agent reasoning and tool use; its network-slicing component directly exercises resource-allocation decisions. |

## Dataset portals & collections

| Resource | Type | Focus | Access | How to use |
|---|---|---|---|---|
| [CRAWDAD Collection on IEEE DataPort](https://www.crawdad.org/) | Dataset collection | Wireless Specific | Registration | Use for historical and measurement-oriented wireless datasets; CRAWDAD is now a collection inside IEEE DataPort rather than a separate active repository. |
| [Hugging Face Datasets Hub](https://huggingface.co/datasets) | Data portal | General | Mixed | Filter by task and search telecom/wireless keywords; inspect dataset cards, licenses, gating, and source provenance before treating a hosted copy as canonical. |
| [IEEE DataPort](https://ieee-dataport.org/) | Data portal | General | Registration | Search with the wireless task name plus modality or technology, then verify each candidate against its dataset paper/documentation before adding it to this catalogue. |
| [Kaggle Datasets & Competitions](https://www.kaggle.com/datasets) | Data portal | General | Registration | Search datasets and competitions separately; competition data may require accepting rules or account-based access even when the metadata page is public. |
| [Mendeley Data](https://data.mendeley.com/) | Data portal | General | Mixed | Search by wireless task, technology, and signal modality; check versions and related-paper metadata to avoid duplicate or derivative records. |
| [OpenML](https://www.openml.org/) | Data portal | General | Mixed | Useful when a wireless dataset has been mirrored into OpenML or when standardized ML task definitions and benchmark suites are more important than domain-specific hosting. |
| [Zenodo](https://zenodo.org/) | Data portal | General | Mixed | Search exact wireless task terms, dataset titles, DOI fragments, authors, or project names; verify that a record contains reusable data rather than only supplementary figures or code. |
