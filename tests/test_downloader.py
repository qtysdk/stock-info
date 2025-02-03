import pytest

from stock_info.downloader import Downloader, build_failed_result
from stock_info import Result


def test_fetch_0056(downloader: Downloader):
    result = downloader.download("0056")
    assert result == Result(
        success=True,
        stock_number="0056",
        dividend=1.07,
        dividend_date="2025/01/17",
        payment_date="2025/02/20",
        meeting_date=None,
        dividend_yield=2.95,
    )


def test_fetch_00713(downloader: Downloader):
    result = downloader.download("00713")
    assert result == Result(
        success=True,
        stock_number="00713",
        dividend=1.4,
        dividend_date="2024/12/17",
        payment_date="2025/01/13",
        meeting_date=None,
        dividend_yield=9.51,
    )


def test_fetch_006208(downloader: Downloader):
    result = downloader.download("006208")
    assert result == Result(
        success=True,
        stock_number="006208",
        dividend=0.9,
        dividend_date="2024/11/18",
        payment_date="2024/12/12",
        meeting_date=None,
        dividend_yield=1.67,
    )


def test_fetch_00878(downloader: Downloader):
    result = downloader.download("00878")
    assert result == Result(
        success=True,
        stock_number="00878",
        dividend=0.55,
        dividend_date="2024/11/18",
        payment_date="2024/12/12",
        meeting_date=None,
        dividend_yield=8.89,
    )


def test_fetch_00919(downloader: Downloader):
    result = downloader.download("00919")
    assert result == Result(
        success=True,
        stock_number="00919",
        dividend=0.72,
        dividend_date="2024/12/20",
        payment_date="2025/01/13",
        meeting_date=None,
        dividend_yield=11.5,
    )


def test_fetch_non_exists(downloader: Downloader):
    with pytest.raises(ValueError) as exec_info:
        downloader.download("C8763")
    assert exec_info.match("curl_command_not_found")
