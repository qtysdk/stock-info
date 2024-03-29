import os

import pytest

from stock_info.cache import Cache
from stock_info.downloader import Downloader


@pytest.fixture(autouse=True)
def enable_fake_downloader():
    os.environ["FAKE_DOWNLOADER"] = "true"
    yield
    del os.environ["FAKE_DOWNLOADER"]


@pytest.fixture
def cache() -> Cache:
    cache = Cache()
    return cache


@pytest.fixture
def downloader() -> Downloader:
    dl = Downloader()
    assert dl.enable_fake
    return dl
