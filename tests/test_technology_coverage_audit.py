from __future__ import annotations

import shutil
from pathlib import Path

import yaml

from scripts.audit_technology_coverage import audit_repository

ROOT = Path(__file__).resolve().parents[1]


def copy_inputs(destination: Path):
    shutil.copytree(ROOT / "data", destination / "data")


def test_repository_technology_audit_is_clean():
    candidates, counts, vocabulary_problems = audit_repository(ROOT)
    assert vocabulary_problems == []
    assert candidates == []
    assert counts["6g"] >= 1


def test_audit_flags_6g_generation_without_technology(tmp_path):
    copy_inputs(tmp_path)
    path = tmp_path / "data" / "datasets" / "deepsense6g.yaml"
    item = yaml.safe_load(path.read_text(encoding="utf-8"))
    item["technologies"] = [value for value in item["technologies"] if value != "6g"]
    path.write_text(yaml.safe_dump(item, sort_keys=False), encoding="utf-8")

    candidates, _, _ = audit_repository(tmp_path)
    assert any(candidate.dataset_id == "deepsense6g" for candidate in candidates)


def test_audit_rejects_isac_as_technology_vocabulary_value(tmp_path):
    copy_inputs(tmp_path)
    path = tmp_path / "data" / "vocabularies.yaml"
    vocab = yaml.safe_load(path.read_text(encoding="utf-8"))
    vocab["technologies"].append({"id": "isac", "name": "ISAC"})
    path.write_text(yaml.safe_dump(vocab, sort_keys=False), encoding="utf-8")

    _, _, problems = audit_repository(tmp_path)
    assert any("must not contain 'isac'" in problem for problem in problems)


def test_audit_rejects_lora_as_peer_technology_value(tmp_path):
    copy_inputs(tmp_path)
    path = tmp_path / "data" / "vocabularies.yaml"
    vocab = yaml.safe_load(path.read_text(encoding="utf-8"))
    vocab["technologies"].append({"id": "lora", "name": "LoRa"})
    path.write_text(yaml.safe_dump(vocab, sort_keys=False), encoding="utf-8")

    _, _, problems = audit_repository(tmp_path)
    assert any("must not contain 'lora'" in problem for problem in problems)
