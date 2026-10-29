import time
from cache_service import CacheService


def test_set_and_get():
    cache = CacheService()
    cache.set("name", "hello")
    assert cache.get("name") == "hello"


def test_missing_key():
    cache = CacheService()
    assert cache.get("missing") is None


def test_delete():
    cache = CacheService()
    cache.set("name", "hello")
    cache.delete("name")
    assert cache.get("name") is None


def test_expiration():
    cache = CacheService()
    cache.set("temporary", "value", ttl=1)
    assert cache.get("temporary") == "value"
    time.sleep(1.1)
    assert cache.get("temporary") is None


def test_clear():
    cache = CacheService()
    cache.set("a", 1)
    cache.set("b", 2)
    cache.clear()
    assert cache.get("a") is None
    assert cache.get("b") is None
