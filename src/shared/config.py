"""Config loading. All tuning lives in YAML so the system is clone-per-client
and tune-without-code."""
from copy import deepcopy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"


def _load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    with open(path) as f:
        return yaml.safe_load(f) or {}


def load_vertical(name: str) -> dict:
    return _load_yaml(CONFIG_DIR / "verticals" / f"{name}.yaml")


def load_geo(name: str) -> dict:
    return _load_yaml(CONFIG_DIR / "geos" / f"{name}.yaml")


def load_scoring(vertical: dict | None = None) -> dict:
    """Base scoring merged with any per-vertical overrides."""
    base = deepcopy(_load_yaml(CONFIG_DIR / "scoring.yaml"))
    overrides = (vertical or {}).get("scoring_overrides") or {}
    for section in ("weights", "thresholds"):
        if section in overrides:
            base.setdefault(section, {}).update(overrides[section])
    return base
