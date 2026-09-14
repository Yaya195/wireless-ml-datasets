from scripts.audit_task_coverage import audit_dataset, spatial_suitability_hints


def active_tasks(*ids):
    return {task_id: {"id": task_id, "status": "active"} for task_id in ids}


def test_audit_flags_explicit_unmapped_task_phrase():
    dataset = {
        "id": "example",
        "name": "Example",
        "description": "Released for localization and beam prediction research.",
        "references": [],
        "tasks": [{"task": "beam-prediction"}],
        "caveats": [],
    }
    candidates = audit_dataset(dataset, active_tasks("localization", "beam-prediction"))
    assert [(candidate.dataset_id, candidate.task_id) for candidate in candidates] == [
        ("example", "localization")
    ]


def test_audit_does_not_flag_existing_mapping():
    dataset = {
        "id": "example",
        "name": "Example",
        "description": "A localization dataset.",
        "references": [],
        "tasks": [{"task": "localization"}],
        "caveats": [],
    }
    assert audit_dataset(dataset, active_tasks("localization")) == []


def test_audit_is_review_only_and_can_surface_deferred_notes():
    dataset = {
        "id": "example",
        "name": "Example",
        "description": "Wireless measurements.",
        "references": [],
        "tasks": [{"task": "channel-estimation", "notes": "Task backfill remains for the final audit."}],
        "caveats": [],
    }
    candidates = audit_dataset(dataset, active_tasks("channel-estimation", "localization"))
    assert len(candidates) == 1
    assert candidates[0].task_id == "manual-review"


def test_audit_does_not_treat_negative_caveat_as_positive_evidence():
    dataset = {
        "id": "example",
        "name": "Example",
        "description": "A signal-classification dataset.",
        "references": [],
        "tasks": [{"task": "signal-classification"}],
        "caveats": [{"text": "Do not infer RF fingerprinting from device identification wording."}],
    }
    assert audit_dataset(dataset, active_tasks("signal-classification", "rf-fingerprinting")) == []


def test_audit_suppresses_generic_localization_for_curated_subtype():
    dataset = {
        "id": "example",
        "name": "Example localization dataset",
        "description": "Device-free localization of a passive target.",
        "references": [],
        "tasks": [{"task": "device-free-localization"}],
        "caveats": [],
    }
    candidates = audit_dataset(
        dataset, active_tasks("localization", "device-free-localization")
    )
    assert candidates == []


def test_audit_flags_strong_ground_truth_signal_without_task_phrase():
    dataset = {
        "id": "example",
        "name": "Example",
        "description": "A set of network measurements.",
        "ground_truth": ["application-label"],
        "references": [],
        "tasks": [],
        "caveats": [],
    }
    candidates = audit_dataset(dataset, active_tasks("traffic-classification"))
    assert [(candidate.dataset_id, candidate.task_id) for candidate in candidates] == [
        ("example", "traffic-classification")
    ]


def test_audit_respects_documented_structural_false_positive():
    dataset = {
        "id": "example",
        "name": "Example",
        "description": "Network observability measurements.",
        "ground_truth": ["application-label"],
        "references": [],
        "tasks": [],
        "caveats": [
            {
                "text": "The application label is contextual metadata and is not by itself evidence of traffic classification."
            }
        ],
    }
    assert audit_dataset(dataset, active_tasks("traffic-classification")) == []


def test_spatial_suitability_flags_navigation_support_without_mapping():
    dataset = {
        "id": "trajectory-radio",
        "name": "Trajectory Radio",
        "modalities": ["wifi-rssi", "imu"],
        "ground_truth": ["position"],
        "temporal_structure": "trajectory",
        "tasks": [{"task": "localization"}],
    }
    hints = spatial_suitability_hints(dataset)
    assert any(hint.use_case == "radio-assisted-navigation" for hint in hints)


def test_spatial_suitability_suppresses_verified_navigation_mapping():
    dataset = {
        "id": "verified-nav",
        "name": "Verified Navigation",
        "modalities": ["wifi-rssi"],
        "ground_truth": ["position", "navigation-action"],
        "temporal_structure": "trajectory",
        "tasks": [{"task": "radio-assisted-navigation"}],
    }
    hints = spatial_suitability_hints(dataset)
    assert not any(hint.use_case == "radio-assisted-navigation" for hint in hints)


def test_spatial_suitability_flags_geometry_rich_radio_slam_candidate():
    dataset = {
        "id": "geometry-radio",
        "name": "Geometry Radio",
        "modalities": ["path-parameters", "scene-geometry"],
        "ground_truth": ["position", "scene-geometry"],
        "temporal_structure": "snapshot",
        "tasks": [{"task": "localization"}],
    }
    hints = spatial_suitability_hints(dataset)
    assert any(hint.use_case == "radio-slam" for hint in hints)


def test_spatial_suitability_allows_snapshot_radio_slam_candidates():
    dataset = {
        "id": "snapshot-geometry",
        "name": "Snapshot Geometry",
        "modalities": ["path-parameters"],
        "ground_truth": ["position", "scene-geometry"],
        "temporal_structure": "snapshot",
        "tasks": [],
    }
    hints = spatial_suitability_hints(dataset)
    assert any(hint.use_case == "radio-slam" for hint in hints)
