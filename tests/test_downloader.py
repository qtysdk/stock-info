import pytest

from stock_info.downloader import Downloader, Result, build_failed_result


def test_fetch_0056(downloader: Downloader):
    result = downloader.download("0056")
    assert result == Result(
        success=True,
        dividend=0.7,
        exDividendDate="2024/01/17",
        dividendPaymentDate="2024/02/21",
        stock_number="0056",
    )


def test_fetch_00878(downloader: Downloader):
    with pytest.raises(ValueError) as exec_info:
        downloader.download("00878")
    assert exec_info.match("curl_command_not_found")


def test_fetch_non_exists(downloader: Downloader):
    result = downloader.download("C8763")
    assert result == build_failed_result("C8763")
