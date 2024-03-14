import pytest

from stock_info.downloader import Downloader, build_failed_result
from stock_info import Result


def test_fetch_0056(downloader: Downloader):
    result = downloader.download("0056")
    assert result == Result(
        success=True,
        stock_number="0056",
        dividend=0.7,
        dividend_date="2024/01/17",
        payment_date="2024/02/21",
        meeting_date=None,
        dividend_yield=1.89,
    )


def test_fetch_00713(downloader: Downloader):
    result = downloader.download("00713")
    assert result == Result(
        success=True,
        stock_number="00713",
        dividend=0.88,
        dividend_date="2024/03/18",
        payment_date=" ",
        meeting_date=None,
        dividend_yield=6.83,
    )


def test_fetch_006208(downloader: Downloader):
    result = downloader.download("006208")
    assert result == Result(
        success=True,
        stock_number="006208",
        dividend=0.861,
        dividend_date="2023/11/16",
        payment_date="2023/12/12",
        meeting_date=None,
        dividend_yield=3.08,
    )


def test_fetch_00878(downloader: Downloader):
    result = downloader.download("00878")
    assert result == Result(
        success=True,
        stock_number="00878",
        dividend=0.4,
        dividend_date="2024/02/27",
        payment_date="2024/03/25",
        meeting_date=None,
        dividend_yield=1.84,
    )


def test_fetch_00919(downloader: Downloader):
    result = downloader.download("00919")
    assert result == Result(
        success=True,
        stock_number="00919",
        dividend=0.55,
        dividend_date="2023/12/18",
        payment_date="2024/01/12",
        meeting_date=None,
        dividend_yield=8.24,
    )


def test_fetch_00929(downloader: Downloader):
    result = downloader.download("00929")
    assert result == Result(
        success=True,
        stock_number="00929",
        dividend=0.13,
        dividend_date="2024/02/29",
        payment_date="2024/03/26",
        meeting_date=None,
        dividend_yield=2.04,
    )


def test_fetch_non_exists(downloader: Downloader):
    with pytest.raises(ValueError) as exec_info:
        downloader.download("C8763")
    assert exec_info.match("curl_command_not_found")
