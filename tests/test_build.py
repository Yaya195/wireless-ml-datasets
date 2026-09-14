from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from scripts.build import (
    GENERATED_DIRECTORY_PATHS,
    GENERATED_FILE_PATHS,
    build,
    check_generated,
)

ROOT = Path(__file__).resolve().parents[1]

def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def generated_files(root: Path):
    files = list((root / "catalog").rglob("*.md"))
    files.append(root / "dist" / "catalog.json")
    return sorted(files)

def copy_build_inputs(destination: Path):
    shutil.copytree(ROOT / "data", destination / "data")
    shutil.copytree(ROOT / "schema", destination / "schema")

def test_build_generates_expected_outputs(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    assert (tmp_path / "catalog" / "README.md").exists()
    assert (tmp_path / "catalog" / "datasets.md").exists()
    assert (tmp_path / "catalog" / "technologies.md").exists()
    assert (tmp_path / "dist" / "catalog.json").exists()
    assert any((tmp_path / "catalog" / "tasks").glob("*.md"))
    assert any((tmp_path / "catalog" / "datasets").glob("*.md"))
    assert any((tmp_path / "catalog" / "technologies").glob("*.md"))

def test_only_populated_task_pages_are_generated(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    generated = {path.stem for path in (tmp_path / "catalog" / "tasks").glob("*.md")}

    expected = set()
    for dataset_path in (tmp_path / "data" / "datasets").glob("*.yaml"):
        import yaml
        item = yaml.safe_load(dataset_path.read_text(encoding="utf-8"))
        expected.update(mapping["task"] for mapping in item["tasks"])

    # Candidate/inactive tasks are not expected, but all current mapped tasks are active.
    assert generated == expected

def test_build_is_deterministic(tmp_path):
    copy_build_inputs(tmp_path)

    build(tmp_path)
    first = {
        str(path.relative_to(tmp_path)): file_hash(path)
        for path in generated_files(tmp_path)
    }

    build(tmp_path)
    second = {
        str(path.relative_to(tmp_path)): file_hash(path)
        for path in generated_files(tmp_path)
    }

    assert first == second

def test_catalog_json_has_expected_top_level_sections(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    payload = json.loads(
        (tmp_path / "dist" / "catalog.json").read_text(encoding="utf-8")
    )

    assert set(payload) == {
        "schema_version",
        "categories",
        "tasks",
        "datasets",
        "collections",
        "resources",
        "technology_index",
        "vocabularies",
    }
    assert payload["datasets"]
    assert payload["tasks"]
    assert payload["vocabularies"]

def test_catalog_json_contains_only_populated_tasks(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    payload = json.loads(
        (tmp_path / "dist" / "catalog.json").read_text(encoding="utf-8")
    )
    task_ids = {task["id"] for task in payload["tasks"]}
    mapped_ids = {
        mapping["task"]
        for dataset in payload["datasets"]
        for mapping in dataset["tasks"]
    }

    assert task_ids == mapped_ids

def test_generated_files_are_current():
    assert check_generated(ROOT) == []


def test_scale_unit_labels_are_human_readable(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    widar = (
        tmp_path
        / "catalog"
        / "datasets"
        / "widar3.md"
    ).read_text(encoding="utf-8")

    assert "Duration Hours" not in widar
    assert "Size Gb" not in widar


def test_task_pages_mark_collection_resources(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    page = (
        tmp_path / "catalog" / "tasks" / "beam-prediction.md"
    ).read_text(encoding="utf-8")

    assert "<sub>Collection</sub>" in page or "<sub>Family</sub>" in page

def test_channel_charting_renders_evaluation_reference(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    page = (
        tmp_path / "catalog" / "tasks" / "channel-charting.md"
    ).read_text(encoding="utf-8")

    assert "Evaluation reference" in page
    assert "Position" in page

def test_radiomapseer_localization_uses_rss_observation(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    page = (
        tmp_path / "catalog" / "tasks" / "localization.md"
    ).read_text(encoding="utf-8")

    radio_map_seer_row = next(
        line for line in page.splitlines()
        if "RadioMapSeer" in line
    )
    assert "RSS" in radio_map_seer_row
    assert "Radio map" in radio_map_seer_row


def test_batch2_opens_new_task_pages(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    expected = {
        "channel-estimation",
        "channel-extrapolation",
        "human-activity-recognition",
        "vital-sign-sensing",
        "resource-allocation",
        "traffic-classification",
    }
    generated = {
        path.stem
        for path in (tmp_path / "catalog" / "tasks").glob("*.md")
    }
    assert expected <= generated


def test_catalog_landing_groups_populated_tasks(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    page = (
        tmp_path / "catalog" / "README.md"
    ).read_text(encoding="utf-8")

    assert "# Browse by wireless research task" in page
    assert "## Channel & CSI" in page
    assert "## Beam Management" in page
    assert "## Localization & Mapping" in page
    assert "## Signal Intelligence" in page
    assert "## Wireless Sensing" in page
    assert "## Network Intelligence" in page
    assert "Channel Estimation" in page
    assert "Traffic Classification" in page

def test_generated_check_detects_stale_file(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    datasets_index = tmp_path / "catalog" / "datasets.md"
    datasets_index.write_text(
        datasets_index.read_text(encoding="utf-8") + "\\nmanual edit\\n",
        encoding="utf-8",
    )

    problems = check_generated(tmp_path)
    expected_path = str(Path("catalog") / "datasets.md")
    assert any(expected_path in problem for problem in problems)


def test_root_readme_contains_generated_featured_table(tmp_path):
    copy_build_inputs(tmp_path)
    shutil.copy2(ROOT / "README.md", tmp_path / "README.md")
    build(tmp_path)

    page = (tmp_path / "README.md").read_text(encoding="utf-8")

    assert "## Featured datasets" in page
    assert "<!-- FEATURED_DATASETS_START -->" in page
    assert "<!-- FEATURED_DATASETS_END -->" in page
    assert "| Dataset | Representative task(s) | Origin | Access |" in page
    assert "[DeepMIMO](catalog/datasets/deepmimo.md)" in page
    assert "[RadioML 2018.01A](catalog/datasets/radioml-2018-01a.md)" in page
    assert "not** a popularity ranking" in page

def test_generated_check_detects_stale_readme_featured_block(tmp_path):
    copy_build_inputs(tmp_path)
    shutil.copy2(ROOT / "README.md", tmp_path / "README.md")
    build(tmp_path)

    readme = tmp_path / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8").replace(
            "[DeepMIMO](catalog/datasets/deepmimo.md)",
            "DeepMIMO",
            1,
        ),
        encoding="utf-8",
    )

    problems = check_generated(tmp_path)
    assert any("README.md" in problem for problem in problems)


def test_batch3_opens_gap_task_pages(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    expected = {
        "csi-feedback",
        "cooperative-localization",
        "device-free-localization",
        "radio-slam",
        "interference-classification",
        "presence-detection",
        "pose-estimation",
        "handover-prediction",
        "network-anomaly-detection",
    }
    generated = {
        path.stem
        for path in (tmp_path / "catalog" / "tasks").glob("*.md")
    }
    assert expected <= generated


def test_generated_artifact_inventory_covers_protected_outputs():
    protected = {
        "catalog/README.md",
        "catalog/datasets.md",
        "catalog/technologies.md",
        "dist/catalog.json",
    }
    assert protected <= set(GENERATED_FILE_PATHS)
    assert {"catalog/tasks", "catalog/datasets", "catalog/technologies"} <= set(
        GENERATED_DIRECTORY_PATHS
    )

def test_generated_check_rejects_manual_dataset_page_edit(tmp_path):
    copy_build_inputs(tmp_path)
    shutil.copy2(ROOT / "README.md", tmp_path / "README.md")
    build(tmp_path)

    page = tmp_path / "catalog" / "datasets" / "deepmimo.md"
    page.write_text(
        page.read_text(encoding="utf-8") + "\nmanual edit\n",
        encoding="utf-8",
    )

    problems = check_generated(tmp_path)
    expected = str(Path("catalog") / "datasets" / "deepmimo.md")
    assert any(expected in problem for problem in problems)


def test_batch4_opens_control_and_forecasting_tasks(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    expected = {
        "power-control",
        "user-scheduling",
        "traffic-prediction",
    }
    generated = {
        path.stem
        for path in (tmp_path / "catalog" / "tasks").glob("*.md")
    }
    assert expected <= generated


def test_batch5_strengthens_thin_task_pages(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    expected_minimums = {
        "channel-estimation": 3,
        "channel-prediction": 3,
        "cooperative-localization": 2,
        "device-free-localization": 2,
        "modulation-recognition": 2,
        "radio-map-estimation": 2,
        "rf-fingerprinting": 4,
        "signal-classification": 2,
        "traffic-classification": 2,
        "user-scheduling": 2,
    }

    for task_id, minimum in expected_minimums.items():
        page = (
            tmp_path / "catalog" / "tasks" / f"{task_id}.md"
        ).read_text(encoding="utf-8")
        marker = "**Datasets in catalogue:** "
        count_line = next(line for line in page.splitlines() if line.startswith(marker))
        count = int(count_line.removeprefix(marker))
        assert count >= minimum, f"{task_id}: expected >= {minimum}, got {count}"


def test_batch6_strengthens_remaining_thin_task_pages(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    expected_minimums = {
        "blockage-prediction": 4,
        "human-activity-recognition": 8,
        "interference-classification": 2,
        "modulation-recognition": 4,
        "network-anomaly-detection": 3,
        "pose-estimation": 3,
        "radio-map-estimation": 3,
        "signal-classification": 3,
        "traffic-prediction": 2,
        "vital-sign-sensing": 3,
    }

    for task_id, minimum in expected_minimums.items():
        page = (
            tmp_path / "catalog" / "tasks" / f"{task_id}.md"
        ).read_text(encoding="utf-8")
        marker = "**Datasets in catalogue:** "
        count_line = next(
            line for line in page.splitlines() if line.startswith(marker)
        )
        count = int(count_line.removeprefix(marker))
        assert count >= minimum, f"{task_id}: expected >= {minimum}, got {count}"


def test_batch7_strengthens_source_sweep_tasks(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    expected_minimums = {
        "beam-selection": 2,
        "channel-prediction": 4,
        "device-free-localization": 3,
        "gesture-recognition": 4,
        "human-activity-recognition": 9,
        "localization": 12,
        "radio-map-estimation": 5,
        "rf-fingerprinting": 7,
        "signal-classification": 4,
        "spectrum-sensing": 3,
    }

    for task_id, minimum in expected_minimums.items():
        page = (
            tmp_path / "catalog" / "tasks" / f"{task_id}.md"
        ).read_text(encoding="utf-8")
        marker = "**Datasets in catalogue:** "
        count_line = next(
            line for line in page.splitlines() if line.startswith(marker)
        )
        count = int(count_line.removeprefix(marker))
        assert count >= minimum, f"{task_id}: expected >= {minimum}, got {count}"


def test_root_readme_contains_generated_catalogue_count(tmp_path):
    copy_build_inputs(tmp_path)
    shutil.copy2(ROOT / "README.md", tmp_path / "README.md")
    build(tmp_path)

    page = (tmp_path / "README.md").read_text(encoding="utf-8")
    dataset_count = len(list((tmp_path / "data" / "datasets").glob("*.yaml")))
    task_page_count = len(list((tmp_path / "catalog" / "tasks").glob("*.md")))

    assert "<!-- CATALOG_STATS_START -->" in page
    assert "<!-- CATALOG_STATS_END -->" in page
    assert f"**{dataset_count} datasets**" in page
    assert f"**{task_page_count} populated wireless tasks**" in page


def test_generated_check_detects_stale_readme_catalogue_count(tmp_path):
    copy_build_inputs(tmp_path)
    shutil.copy2(ROOT / "README.md", tmp_path / "README.md")
    build(tmp_path)

    readme = tmp_path / "README.md"
    dataset_count = len(list((tmp_path / "data" / "datasets").glob("*.yaml")))
    readme.write_text(
        readme.read_text(encoding="utf-8").replace(
            f"{dataset_count} datasets", "999 datasets", 1
        ),
        encoding="utf-8",
    )

    problems = check_generated(tmp_path)
    assert any("README.md" in problem for problem in problems)


def test_v1_resources_and_collection_are_generated(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    assert (tmp_path / "catalog" / "resources.md").exists()
    collection_page = (
        tmp_path / "catalog" / "collections" / "llm-foundation-model-resources.md"
    )
    assert collection_page.exists()
    text = collection_page.read_text(encoding="utf-8")
    assert "TeleLogs" in text
    assert "TeleQnA" in text
    assert "WirelessBench" in text
    assert "wireless research task" in text


def test_supporting_resources_do_not_inflate_core_dataset_count(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    payload = json.loads((tmp_path / "dist" / "catalog.json").read_text(encoding="utf-8"))
    dataset_count = len(list((tmp_path / "data" / "datasets").glob("*.yaml")))
    resource_count = len(list((tmp_path / "data" / "resources").glob("*.yaml")))

    assert len(payload["datasets"]) == dataset_count
    assert len(payload["resources"]) == resource_count
    assert {item["id"] for item in payload["datasets"]}.isdisjoint(
        {item["id"] for item in payload["resources"]}
    )


def test_readme_reports_supporting_resource_count(tmp_path):
    copy_build_inputs(tmp_path)
    shutil.copy2(ROOT / "README.md", tmp_path / "README.md")
    build(tmp_path)

    page = (tmp_path / "README.md").read_text(encoding="utf-8")
    resource_count = len(list((tmp_path / "data" / "resources").glob("*.yaml")))
    assert f"**{resource_count} curated benchmark, foundation-model, and discovery resources**" in page


def test_task_page_can_surface_supporting_resource_without_counting_it_as_dataset(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    page = (tmp_path / "catalog" / "tasks" / "resource-allocation.md").read_text(encoding="utf-8")
    assert "WirelessBench" in page
    marker = "**Datasets in catalogue:** "
    count_line = next(line for line in page.splitlines() if line.startswith(marker))
    dataset_count_on_page = int(count_line.removeprefix(marker))

    expected = 0
    for dataset_path in (tmp_path / "data" / "datasets").glob("*.yaml"):
        import yaml
        item = yaml.safe_load(dataset_path.read_text(encoding="utf-8"))
        expected += any(mapping["task"] == "resource-allocation" for mapping in item["tasks"])
    assert dataset_count_on_page == expected


def test_llm_collection_is_linked_from_core_dataset_page(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    page = (tmp_path / "catalog" / "datasets" / "telelogs.md").read_text(encoding="utf-8")
    assert "LLM & Foundation Model Resources" in page
    assert "../collections/llm-foundation-model-resources.md" in page

def test_phase8_technology_index_and_6g_page_are_generated(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    index = (tmp_path / "catalog" / "technologies.md").read_text(encoding="utf-8")
    page = (tmp_path / "catalog" / "technologies" / "6g.md").read_text(encoding="utf-8")

    assert "# Browse by wireless technology" in index
    assert "[6G](technologies/6g.md)" in index
    assert "DeepSense 6G" in page
    assert "CONVERGE ICASSP 2026 Multimodal 6G Dataset" in page
    assert "26 GHz Communication Channel Dataset for Domain Shift Invariant Blockage Prediction" not in page


def test_phase8_json_contains_technology_index_without_changing_core_counts(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    payload = json.loads((tmp_path / "dist" / "catalog.json").read_text(encoding="utf-8"))
    sixg = next(item for item in payload["technology_index"] if item["id"] == "6g")
    dataset_count = len(list((tmp_path / "data" / "datasets").glob("*.yaml")))

    assert len(payload["datasets"]) == dataset_count
    assert sixg["dataset_count"] == len(sixg["dataset_ids"])
    assert "converge-icassp2026" in sixg["dataset_ids"]
    assert "ku-leuven-26ghz-blockage" not in sixg["dataset_ids"]


def test_root_readme_links_secondary_technology_browse(tmp_path):
    copy_build_inputs(tmp_path)
    shutil.copy2(ROOT / "README.md", tmp_path / "README.md")
    build(tmp_path)

    page = (tmp_path / "README.md").read_text(encoding="utf-8")
    assert "[Browse by wireless technology](catalog/technologies.md)" in page



def test_phase9_radio_assisted_navigation_page_is_generated(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    page = (
        tmp_path / "catalog" / "tasks" / "radio-assisted-navigation.md"
    ).read_text(encoding="utf-8")
    assert "RA-CD: Robot-Aided Wi-Fi Localization and Navigation Dataset" in page
    assert "PIRL-WIN" in page
    assert "Related supporting resources" in page


def test_phase9_radio_slam_page_surfaces_verified_datasets_and_temporal_structure(tmp_path):
    copy_build_inputs(tmp_path)
    build(tmp_path)

    page = (tmp_path / "catalog" / "tasks" / "radio-slam.md").read_text(
        encoding="utf-8"
    )
    assert "DeepMIMO" in page
    assert "P2SLAM Wi-Fi SLAM Dataset Collection" in page
    assert "Millimeter-Wave Radio SLAM: 60 GHz Indoor Sensing Dataset" in page
    assert "Temporal structure" in page
