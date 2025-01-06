from stock_info.cache import Cache


def test_cache(cache: Cache):

    data = cache.put_item({"stock_number": "C8763.1"})
    fetched = cache.get_item("C8763.1")

    assert data == fetched


def test_cache_item_not_found(cache: Cache):
    fetched = cache.get_item("C8763._not_found")
    assert fetched is None


def test_cached_downloading():
    from stock_info.handler import download_or_get_from_cache

    result = download_or_get_from_cache("00878")
    assert result is not None


def test_cache_delete_item(cache: Cache):
    numbers = [
        "0056",
        "006208",
        "00631L",
        "00713",
        "00878",
        "00919",
        "1513",
        "2330",
        "2412",
        "2880",
        "2887",
        "2890",
        "2892",
    ]
    for number in numbers:
        cache.delete_item(number)
        cache.delete_item(f"{number}_yield")
        cache.delete_item(f"{number}_yield_not_such_key")
