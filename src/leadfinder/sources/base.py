from abc import ABC, abstractmethod

from ...shared.models import Lead


class LeadSource(ABC):
    """All lead sources share this interface so they're swappable: mock today,
    Google Places when you have a key, Apollo later."""

    name = "base"

    @abstractmethod
    def search(self, vertical: dict, geo: dict, limit: int = 60) -> list[Lead]:
        ...
