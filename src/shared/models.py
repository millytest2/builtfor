from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Lead:
    """A prospect's online-presence snapshot. Sources fill what they can;
    missing fields degrade gracefully in the scorer."""
    name: str
    category: str = ""
    source: str = ""
    place_id: Optional[str] = None
    address: str = ""
    phone: Optional[str] = None
    website: Optional[str] = None
    google_rating: Optional[float] = None
    review_count: int = 0
    photos_count: int = 0
    categories: list = field(default_factory=list)
    has_hours: bool = False
    claimed: bool = True
    latest_review_age_days: Optional[int] = None

    # Filled by the scorer
    presence_score: int = 0
    priority: str = ""
    top_problems: list = field(default_factory=list)
    score_breakdown: dict = field(default_factory=dict)
