import time
from rate_limiter import RateLimiter

def test_allows_requests_within_limit():
    limiter = RateLimiter(max_requests=3, window_seconds=60)
    assert limiter.is_allowed("client-1")
    assert limiter.is_allowed("client-1")
    assert limiter.is_allowed("client-1")


def test_rejects_requests_over_limit():
    limiter = RateLimiter(max_requests=2, window_seconds=60)
    assert limiter.is_allowed("client-1")
    assert limiter.is_allowed("client-1")
    assert not limiter.is_allowed("client-1")


def test_clients_have_independent_limits():
    limiter = RateLimiter(max_requests=1, window_seconds=60)
    assert limiter.is_allowed("client-1")
    assert not limiter.is_allowed("client-1")
    assert limiter.is_allowed("client-2")


def test_limit_resets_after_window():
    limiter = RateLimiter(max_requests=1, window_seconds=1)
    assert limiter.is_allowed("client-1")
    assert not limiter.is_allowed("client-1")
    time.sleep(1.1)
    assert limiter.is_allowed("client-1")
