import pytest

from src.leadfinder.export import export_csv
from src.shared.models import Lead


def _leads(n):
    return [Lead(name=f"Biz {i}", presence_score=50) for i in range(n)]


def test_refuses_to_shrink_existing_sheet(tmp_path):
    path = tmp_path / "leads.csv"
    export_csv(_leads(20), str(path))
    with pytest.raises(SystemExit):
        export_csv(_leads(3), str(path))
    # original pull survives
    assert sum(1 for _ in open(path)) - 1 == 20


def test_force_allows_shrink(tmp_path):
    path = tmp_path / "leads.csv"
    export_csv(_leads(20), str(path))
    export_csv(_leads(3), str(path), force=True)
    assert sum(1 for _ in open(path)) - 1 == 3


def test_growing_a_sheet_is_fine(tmp_path):
    path = tmp_path / "leads.csv"
    export_csv(_leads(5), str(path))
    export_csv(_leads(40), str(path))
    assert sum(1 for _ in open(path)) - 1 == 40
