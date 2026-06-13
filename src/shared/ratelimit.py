import time


class RateLimiter:
    """Minimal client-side throttle to stay within API quotas / ToS."""

    def __init__(self, calls_per_sec: float = 5.0):
        self.min_interval = 1.0 / calls_per_sec if calls_per_sec > 0 else 0.0
        self._last = 0.0

    def wait(self) -> None:
        now = time.monotonic()
        delta = now - self._last
        if delta < self.min_interval:
            time.sleep(self.min_interval - delta)
        self._last = time.monotonic()
