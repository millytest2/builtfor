from src.leadfinder.scorer import score_lead
from src.shared import config
from src.shared.models import Lead

SCORING = config.load_scoring()


def test_no_website_is_high_priority():
    lead = score_lead(Lead(name="No Site Co", website=None, review_count=2,
                           photos_count=0, has_hours=False), SCORING)
    assert lead.presence_score >= SCORING["thresholds"]["priority_high"]
    assert lead.priority == "high"
    assert any("website" in p.lower() for p in lead.top_problems)


def test_strong_presence_is_low_priority():
    lead = score_lead(Lead(name="Solid Co", website="https://x.com",
                           google_rating=4.9, review_count=200, photos_count=30,
                           has_hours=True, latest_review_age_days=5), SCORING)
    assert lead.presence_score == 0
    assert lead.priority == "low"


def test_few_reviews_flagged():
    lead = score_lead(Lead(name="Quiet Co", website="https://x.com",
                           google_rating=4.8, review_count=3, photos_count=10,
                           has_hours=True, latest_review_age_days=10), SCORING)
    assert lead.score_breakdown["low_reviews"] > 0
    assert any("review" in p.lower() for p in lead.top_problems)


def test_score_capped_0_100():
    lead = score_lead(Lead(name="Worst", website=None, google_rating=3.0,
                           review_count=0, photos_count=0, has_hours=False,
                           latest_review_age_days=500), SCORING)
    assert 0 <= lead.presence_score <= 100
