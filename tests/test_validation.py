import shutil
from pathlib import Path

import yaml

from scripts.validate import validate_repository

ROOT = Path(__file__).resolve().parents[1]

def test_repository_validation_passes():
    assert validate_repository(ROOT) == []

def test_dataset_ids_match_filenames():
    for path in (ROOT / "data" / "datasets").glob("*.yaml"):
        item = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert item["id"] == path.stem

def test_every_dataset_has_at_least_one_task():
    for path in (ROOT / "data" / "datasets").glob("*.yaml"):
        item = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert item["tasks"], f"{path.name} has no task mappings"

def test_every_task_mapping_has_evidence():
    for path in (ROOT / "data" / "datasets").glob("*.yaml"):
        item = yaml.safe_load(path.read_text(encoding="utf-8"))
        for mapping in item["tasks"]:
            assert mapping["evidence"], (
                f"{path.name}: task {mapping['task']} has no evidence"
            )


def test_every_dataset_has_explicit_identity():
    for path in (ROOT / "data" / "datasets").glob("*.yaml"):
        item = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert "identity" in item
        assert "canonical_url" in item["identity"]
        assert "version" in item["identity"]
        assert "external_ids" in item["identity"]


def test_channel_charting_does_not_fake_position_as_target():
    for dataset_id in ("dichasus", "caez"):
        path = ROOT / "data" / "datasets" / f"{dataset_id}.yaml"
        item = yaml.safe_load(path.read_text(encoding="utf-8"))
        mapping = next(
            entry for entry in item["tasks"]
            if entry["task"] == "channel-charting"
        )
        assert mapping["targets"] == []
        assert mapping["evaluation_reference"] == ["position"]

def test_generic_frequency_regimes_do_not_mix_3gpp_ranges():
    vocab = yaml.safe_load(
        (ROOT / "data" / "vocabularies.yaml").read_text(encoding="utf-8")
    )
    regimes = {entry["id"] for entry in vocab["frequency_regimes"]}
    assert "fr1" not in regimes
    assert "fr2" not in regimes


def test_batch2_network_tasks_are_active():
    for task_id in ("resource-allocation", "traffic-classification"):
        path = ROOT / "data" / "tasks" / f"{task_id}.yaml"
        item = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert item["status"] == "active"

def test_batch2_ground_truth_vocabulary_is_controlled():
    vocab = yaml.safe_load(
        (ROOT / "data" / "vocabularies.yaml").read_text(encoding="utf-8")
    )
    values = {entry["id"] for entry in vocab["ground_truth"]}
    assert {
        "activity-label",
        "respiratory-motion",
        "application-label",
        "signal-class",
    } <= values


def test_featured_dataset_selection_is_compact():
    featured = []
    for path in (ROOT / "data" / "datasets").glob("*.yaml"):
        item = yaml.safe_load(path.read_text(encoding="utf-8"))
        if item.get("featured"):
            featured.append(item["id"])

    assert 10 <= len(featured) <= 15


def test_batch3_ground_truth_and_range_vocabulary():
    vocab = yaml.safe_load(
        (ROOT / "data" / "vocabularies.yaml").read_text(encoding="utf-8")
    )
    modalities = {entry["id"] for entry in vocab["modalities"]}
    ground_truth = {entry["id"] for entry in vocab["ground_truth"]}

    assert "range" in modalities
    assert {
        "presence-label",
        "pose",
        "handover-event",
        "anomaly-label",
        "interference-label",
    } <= ground_truth

def test_radio_slam_exposes_pose_and_mapping_outputs():
    path = ROOT / "data" / "datasets" / "tampere-60ghz-radio-slam.yaml"
    item = yaml.safe_load(path.read_text(encoding="utf-8"))
    mapping = next(entry for entry in item["tasks"] if entry["task"] == "radio-slam")

    assert set(mapping["targets"]) == {"position", "scene-geometry"}
    assert set(mapping["evaluation_reference"]) == {"position", "scene-geometry"}


def test_batch4_control_tasks_are_active():
    for task_id in ("power-control", "user-scheduling"):
        item = yaml.safe_load(
            (ROOT / "data" / "tasks" / f"{task_id}.yaml").read_text(
                encoding="utf-8"
            )
        )
        assert item["status"] == "active"

def test_batch4_ground_truth_vocabulary():
    vocab = yaml.safe_load(
        (ROOT / "data" / "vocabularies.yaml").read_text(encoding="utf-8")
    )
    values = {entry["id"] for entry in vocab["ground_truth"]}
    assert {"power-allocation", "traffic-volume"} <= values


def test_batch5_crosses_launch_dataset_threshold():
    records = list((ROOT / "data" / "datasets").glob("*.yaml"))
    assert len(records) >= 50


def test_batch6_reaches_65_dataset_records():
    records = list((ROOT / "data" / "datasets").glob("*.yaml"))
    assert len(records) >= 65


def test_batch7_reaches_80_dataset_records_and_adds_imu():
    records = list((ROOT / "data" / "datasets").glob("*.yaml"))
    assert len(records) >= 80

    vocab = yaml.safe_load(
        (ROOT / "data" / "vocabularies.yaml").read_text(encoding="utf-8")
    )
    modalities = {entry["id"] for entry in vocab["modalities"]}
    assert "imu" in modalities


def test_batch8_crosses_100_dataset_records():
    records = list((ROOT / "data" / "datasets").glob("*.yaml"))
    assert len(records) >= 103


def _copy_validation_inputs(destination: Path):
    shutil.copytree(ROOT / "data", destination / "data")
    shutil.copytree(ROOT / "schema", destination / "schema")


def test_v1_has_expected_collection_and_supporting_resources():
    collections = list((ROOT / "data" / "collections").glob("*.yaml"))
    resources = list((ROOT / "data" / "resources").glob("*.yaml"))
    assert {path.stem for path in collections} == {"llm-foundation-model-resources"}
    assert len(resources) >= 18


def test_validation_rejects_unknown_resource_collection(tmp_path):
    _copy_validation_inputs(tmp_path)
    resource_path = tmp_path / "data" / "resources" / "teleqna.yaml"
    item = yaml.safe_load(resource_path.read_text(encoding="utf-8"))
    item["collections"] = ["does-not-exist"]
    resource_path.write_text(yaml.safe_dump(item, sort_keys=False), encoding="utf-8")

    failures = validate_repository(tmp_path)
    assert any("unknown collection 'does-not-exist'" in failure for failure in failures)


def test_validation_rejects_missing_resource_task_evidence(tmp_path):
    _copy_validation_inputs(tmp_path)
    resource_path = tmp_path / "data" / "resources" / "wirelessbench.yaml"
    item = yaml.safe_load(resource_path.read_text(encoding="utf-8"))
    item["task_links"][0]["evidence"] = ["missing-ref"]
    resource_path.write_text(yaml.safe_dump(item, sort_keys=False), encoding="utf-8")

    failures = validate_repository(tmp_path)
    assert any("missing evidence id 'missing-ref'" in failure for failure in failures)

def test_phase8_technology_vocabulary_keeps_semantic_levels_clean():
    vocab = yaml.safe_load(
        (ROOT / "data" / "vocabularies.yaml").read_text(encoding="utf-8")
    )
    technologies = {entry["id"] for entry in vocab["technologies"]}

    assert "6g" in technologies
    assert "lorawan" in technologies
    assert "lora" not in technologies
    assert "isac" not in technologies


def test_phase8_reaches_107_core_datasets():
    records = list((ROOT / "data" / "datasets").glob("*.yaml"))
    assert len(records) >= 107


def test_6g_technology_and_generation_context_are_synchronized():
    for path in (ROOT / "data" / "datasets").glob("*.yaml"):
        item = yaml.safe_load(path.read_text(encoding="utf-8"))
        has_technology = "6g" in item.get("technologies", [])
        has_context = "6g" in item.get("generation_contexts", [])
        assert has_technology == has_context, path.name


def test_converge_has_only_released_evidence_backed_tasks():
    item = yaml.safe_load(
        (ROOT / "data" / "datasets" / "converge-icassp2026.yaml").read_text(
            encoding="utf-8"
        )
    )
    assert {mapping["task"] for mapping in item["tasks"]} == {
        "blockage-prediction",
        "localization",
        "channel-prediction",
    }
    assert "beam-prediction" not in {mapping["task"] for mapping in item["tasks"]}



def test_phase9_spatial_intelligence_vocabulary_and_task_are_controlled():
    vocab = yaml.safe_load(
        (ROOT / "data" / "vocabularies.yaml").read_text(encoding="utf-8")
    )
    modalities = {entry["id"] for entry in vocab["modalities"]}
    ground_truth = {entry["id"] for entry in vocab["ground_truth"]}

    assert {"odometry", "gnss", "snr"} <= modalities
    assert {"scene-geometry", "orientation", "velocity", "navigation-action"} <= ground_truth

    task = yaml.safe_load(
        (ROOT / "data" / "tasks" / "radio-assisted-navigation.yaml").read_text(
            encoding="utf-8"
        )
    )
    assert task["status"] == "active"
    assert task["category"] == "localization-mapping"


def test_phase9_deepmimo_is_6g_and_radio_slam_evidence_backed():
    item = yaml.safe_load(
        (ROOT / "data" / "datasets" / "deepmimo.yaml").read_text(encoding="utf-8")
    )
    assert "6g" in item["technologies"]
    assert "6g" in item["generation_contexts"]
    assert "scene-geometry" in item["ground_truth"]
    slam = next(mapping for mapping in item["tasks"] if mapping["task"] == "radio-slam")
    assert slam["evidence"]
    assert {"position", "scene-geometry"} <= set(slam["targets"])


def test_phase9_verified_radio_slam_and_navigation_resources():
    p2slam = yaml.safe_load(
        (ROOT / "data" / "datasets" / "p2slam-wifi-slam.yaml").read_text(encoding="utf-8")
    )
    assert "radio-slam" in {mapping["task"] for mapping in p2slam["tasks"]}

    ra_cd = yaml.safe_load(
        (ROOT / "data" / "datasets" / "ra-cd-wifi-navigation.yaml").read_text(encoding="utf-8")
    )
    assert {"localization", "radio-assisted-navigation"} <= {
        mapping["task"] for mapping in ra_cd["tasks"]
    }

    hymn = yaml.safe_load(
        (ROOT / "data" / "datasets" / "hymn.yaml").read_text(encoding="utf-8")
    )
    assert "localization" in {mapping["task"] for mapping in hymn["tasks"]}
    assert "radio-assisted-navigation" not in {mapping["task"] for mapping in hymn["tasks"]}

    pirl = yaml.safe_load(
        (ROOT / "data" / "resources" / "pirl-win.yaml").read_text(encoding="utf-8")
    )
    assert any(link["task"] == "radio-assisted-navigation" for link in pirl["task_links"])
