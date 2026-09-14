from __future__ import annotations

import argparse
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

# Deliberately explicit phrases. This is a review aid, not an automatic mapper.
TASK_HINTS: dict[str, tuple[str, ...]] = {
    "localization": ("localization", "localisation", "positioning", "location recognition"),
    "cooperative-localization": (
        "cooperative localization",
        "collaborative localization",
        "anchor-free localization",
    ),
    "device-free-localization": (
        "device-free localization",
        "passive localization",
    ),
    "radio-slam": ("radio slam", "radio-slam", "channel-slam", "multipath-assisted slam"),
    "radio-assisted-navigation": (
        "radio-assisted navigation",
        "wireless-assisted navigation",
        "wireless indoor navigation",
        "wi-fi-based indoor localization and navigation",
        "wifi-based indoor localization and navigation",
    ),
    "radio-map-estimation": (
        "radio map estimation",
        "radio-map estimation",
        "pathloss map",
        "path-loss map",
        "radio environment map",
    ),
    "channel-estimation": ("channel estimation",),
    "channel-prediction": ("channel prediction", "csi prediction"),
    "channel-extrapolation": (
        "channel extrapolation",
        "frequency extrapolation",
        "spatial extrapolation",
    ),
    "channel-charting": ("channel charting",),
    "csi-feedback": ("csi feedback", "csi compression"),
    "beam-selection": ("beam selection", "beam recommendation"),
    "beam-prediction": ("beam prediction",),
    "beam-tracking": ("beam tracking",),
    "blockage-prediction": ("blockage prediction",),
    "spectrum-sensing": ("spectrum sensing", "spectrum occupancy"),
    "interference-classification": (
        "interference classification",
        "jamming detection",
        "jammer classification",
    ),
    "modulation-recognition": (
        "modulation recognition",
        "automatic modulation classification",
        "modulation classification",
    ),
    "signal-classification": ("signal classification", "waveform classification"),
    "rf-fingerprinting": (
        "rf fingerprinting",
        "radio-frequency fingerprinting",
        "radio frequency fingerprinting",
        "device fingerprint",
        "emitter identification",
    ),
    "human-activity-recognition": ("human activity recognition", "activity recognition"),
    "gesture-recognition": ("gesture recognition",),
    "presence-detection": ("presence detection", "occupancy detection"),
    "vital-sign-sensing": ("vital sign", "breathing", "respiration", "heart rate"),
    "pose-estimation": ("pose estimation", "human pose"),
    "resource-allocation": ("resource allocation", "radio resource management"),
    "user-scheduling": ("user scheduling", "scheduling policy", "scheduler selection"),
    "power-control": ("power control", "power allocation"),
    "handover-prediction": ("handover prediction", "handoff prediction"),
    "mobility-prediction": ("mobility prediction", "position prediction", "trajectory prediction"),
    "traffic-prediction": ("traffic prediction", "traffic forecasting"),
    "traffic-classification": ("traffic classification",),
    "network-anomaly-detection": ("anomaly detection", "intrusion detection"),
    "network-fault-diagnosis": (
        "fault diagnosis",
        "fault classification",
        "root cause identification",
        "root-cause identification",
        "failure cause",
    ),
}

DEFERRED_PHRASES = ("backfill", "final audit", "not added as catalogue", "not added")


@dataclass(frozen=True)
class Candidate:
    dataset_id: str
    dataset_name: str
    task_id: str
    reason: str


@dataclass(frozen=True)
class SpatialSuitabilityHint:
    dataset_id: str
    dataset_name: str
    use_case: str
    reason: str


RADIO_MODALITIES = {
    "iq",
    "channel-matrix",
    "path-parameters",
    "wifi-rssi",
    "rss",
    "snr",
    "wifi-csi",
    "cir",
    "radio-map",
    "range",
}


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_datasets(root: Path) -> list[dict]:
    return [load_yaml(path) for path in sorted((root / "data" / "datasets").glob("*.yaml"))]


def load_tasks(root: Path) -> dict[str, dict]:
    tasks = {}
    for path in sorted((root / "data" / "tasks").glob("*.yaml")):
        task = load_yaml(path)
        tasks[task["id"]] = task
    return tasks


def evidence_text(dataset: dict) -> str:
    chunks: list[str] = [
        dataset.get("name", ""),
        dataset.get("description", ""),
        " ".join(dataset.get("aliases", [])),
    ]
    for ref in dataset.get("references", []):
        chunks.extend([ref.get("title") or "", ref.get("notes") or ""])
    for mapping in dataset.get("tasks", []):
        chunks.extend([mapping.get("scope") or "", mapping.get("notes") or ""])
    return " ".join(chunks).lower()


def audit_dataset(dataset: dict, tasks: dict[str, dict]) -> list[Candidate]:
    mapped = {mapping["task"] for mapping in dataset.get("tasks", [])}
    text = evidence_text(dataset)
    caveat_text = " ".join(
        caveat.get("text") or "" for caveat in dataset.get("caveats", [])
    ).lower()
    candidates: list[Candidate] = []

    specialized_localization = {"cooperative-localization", "device-free-localization", "radio-slam"}

    for task_id, phrases in TASK_HINTS.items():
        if task_id in mapped or task_id not in tasks or tasks[task_id].get("status") != "active":
            continue
        # Do not flag the generic localization task solely because a record is already
        # explicitly curated under a more specific localization subtype. A curator can
        # still add both when distinct subsets/usages justify both mappings.
        if task_id == "localization" and mapped.intersection(specialized_localization):
            continue
        hits = [phrase for phrase in phrases if phrase in text]
        negated_in_caveat = any(
            phrase in caveat_text
            for phrase in phrases
        ) and any(
            marker in caveat_text
            for marker in ("does not", "do not", "not mapped", "not infer", "not by itself")
        )
        if hits and not negated_in_caveat:
            candidates.append(
                Candidate(
                    dataset_id=dataset["id"],
                    dataset_name=dataset["name"],
                    task_id=task_id,
                    reason="explicit phrase: " + ", ".join(hits),
                )
            )

    # Strong metadata signals are useful when prose does not repeat the task name.
    # They remain review-only: a target label alone is never sufficient evidence.
    ground_truth = set(dataset.get("ground_truth", []))
    structural_hints = {
        "radio-map": "radio-map-estimation",
        "application-label": "traffic-classification",
        "spectrum-occupancy": "spectrum-sensing",
        "handover-event": "handover-prediction",
        "traffic-volume": "traffic-prediction",
        "power-allocation": "power-control",
    }
    for label, task_id in structural_hints.items():
        task_phrase = task_id.replace("-", " ")
        task_named_in_caveat = task_phrase in caveat_text or task_id in caveat_text
        structurally_excluded = (
            task_named_in_caveat
            and any(
                marker in caveat_text
                for marker in (
                    "does not",
                    "do not",
                    "not mapped",
                    "not infer",
                    "not by itself",
                    "no ",
                )
            )
        )
        if (
            label in ground_truth
            and task_id not in mapped
            and task_id in tasks
            and tasks[task_id].get("status") == "active"
            and not structurally_excluded
            and not any(c.task_id == task_id for c in candidates)
        ):
            candidates.append(
                Candidate(
                    dataset_id=dataset["id"],
                    dataset_name=dataset["name"],
                    task_id=task_id,
                    reason=f"ground-truth signal: {label}",
                )
            )

    # Curators sometimes intentionally defer a mapping during expansion. Surface
    # those records even when the exact target task phrase was not captured above.
    deferred_text = text + " " + caveat_text
    if any(phrase in deferred_text for phrase in DEFERRED_PHRASES) and not any(
        c.dataset_id == dataset["id"] for c in candidates
    ):
        candidates.append(
            Candidate(
                dataset_id=dataset["id"],
                dataset_name=dataset["name"],
                task_id="manual-review",
                reason="record contains an explicit deferred/backfill note",
            )
        )

    return candidates


def spatial_suitability_hints(dataset: dict) -> list[SpatialSuitabilityHint]:
    """Return informational spatial-use hints without asserting task membership."""
    mapped = {mapping["task"] for mapping in dataset.get("tasks", [])}
    modalities = set(dataset.get("modalities", []))
    ground_truth = set(dataset.get("ground_truth", []))
    temporal = dataset.get("temporal_structure")
    hints: list[SpatialSuitabilityHint] = []

    if (
        "radio-assisted-navigation" not in mapped
        and temporal in {"sequence", "trajectory", "mixed"}
        and "position" in ground_truth
        and modalities.intersection(RADIO_MODALITIES)
    ):
        hints.append(
            SpatialSuitabilityHint(
                dataset_id=dataset["id"],
                dataset_name=dataset["name"],
                use_case="radio-assisted-navigation",
                reason="sequential/trajectory radio data with position ground truth",
            )
        )

    has_radio_geometry = (
        "path-parameters" in modalities
        and (
            "position" in modalities
            or "scene-geometry" in modalities
            or "position" in ground_truth
            or "scene-geometry" in ground_truth
        )
    )
    has_radio_robotics = (
        "odometry" in modalities
        and bool(modalities.intersection({"wifi-csi", "range", "path-parameters"}))
        and "position" in ground_truth
    )
    if "radio-slam" not in mapped and (has_radio_geometry or has_radio_robotics):
        hints.append(
            SpatialSuitabilityHint(
                dataset_id=dataset["id"],
                dataset_name=dataset["name"],
                use_case="radio-slam",
                reason="radio-geometric/robotics fields could support SLAM research",
            )
        )

    return hints


def collect_spatial_suitability_hints(root: Path = ROOT) -> list[SpatialSuitabilityHint]:
    return [
        hint
        for dataset in load_datasets(root)
        for hint in spatial_suitability_hints(dataset)
    ]


def audit(root: Path = ROOT) -> tuple[list[Candidate], list[str]]:
    datasets = load_datasets(root)
    tasks = load_tasks(root)
    candidates = [candidate for dataset in datasets for candidate in audit_dataset(dataset, tasks)]

    counts = {task_id: 0 for task_id in tasks}
    for dataset in datasets:
        for mapping in dataset.get("tasks", []):
            counts[mapping["task"]] = counts.get(mapping["task"], 0) + 1

    zero_coverage = sorted(
        task_id
        for task_id, task in tasks.items()
        if task.get("status") == "active" and counts.get(task_id, 0) == 0
    )
    return candidates, zero_coverage


def print_report(
    candidates: Iterable[Candidate],
    zero_coverage: Iterable[str],
    suitability_hints: Iterable[SpatialSuitabilityHint] = (),
    *,
    show_suitability: bool = False,
) -> None:
    candidates = list(candidates)
    zero_coverage = list(zero_coverage)
    suitability_hints = list(suitability_hints)

    print(f"Task-coverage audit: {len(candidates)} candidate mapping(s) require review.")
    for candidate in candidates:
        print(
            f"REVIEW {candidate.dataset_id} -> {candidate.task_id}: "
            f"{candidate.reason}"
        )

    if zero_coverage:
        print()
        print("Active tasks with zero mapped datasets:")
        for task_id in zero_coverage:
            print(f" - {task_id}")

    if suitability_hints:
        print()
        print(
            f"Informational spatial-suitability hints: {len(suitability_hints)} "
            "(not verified task mappings)."
        )
        if show_suitability:
            for hint in suitability_hints:
                print(
                    f"SUITABILITY {hint.dataset_id} -> {hint.use_case}: "
                    f"{hint.reason}"
                )
        else:
            print("Use --show-suitability to list them.")

    print()
    print(
        "This audit never modifies dataset records. Verify authoritative evidence "
        "before adding a mapping; suitability hints are not task evidence."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag possible missing Dataset↔Task mappings for curator review."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root (defaults to current project root).",
    )
    parser.add_argument(
        "--show-suitability",
        action="store_true",
        help="List informational Radio-SLAM/navigation suitability hints.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    candidates, zero_coverage = audit(root)
    hints = collect_spatial_suitability_hints(root)
    print_report(
        candidates,
        zero_coverage,
        hints,
        show_suitability=args.show_suitability,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
