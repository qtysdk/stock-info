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


def test_fetch_00713(downloader: Downloader):
    result = downloader.download("00713")
    assert result == Result(
        success=True,
        stock_number="00713",
        dividend=0.88,
        exDividendDate="2024/03/18",
        dividendPaymentDate=" ",
    )


def test_fetch_006208(downloader: Downloader):
    result = downloader.download("006208")
    assert result == Result(
        success=True,
        stock_number="006208",
        dividend=0.861,
        exDividendDate="2023/11/16",
        dividendPaymentDate="2023/12/12",
    )


def test_fetch_00878(downloader: Downloader):
    result = downloader.download("00878")
    assert result == Result(
        success=True,
        stock_number="00878",
        dividend=0.4,
        exDividendDate="2024/02/27",
        dividendPaymentDate="2024/03/25",
    )


def test_fetch_00919(downloader: Downloader):
    result = downloader.download("00919")
    assert result == Result(
        success=True,
        stock_number="00919",
        dividend=0.55,
        exDividendDate="2023/12/18",
        dividendPaymentDate="2024/01/12",
    )


def test_fetch_00929(downloader: Downloader):
    result = downloader.download("00929")
    assert result == Result(
        success=True,
        stock_number="00929",
        dividend=0.13,
        exDividendDate="2024/02/29",
        dividendPaymentDate="2024/03/26",
    )


def test_fetch_non_exists(downloader: Downloader):
    with pytest.raises(ValueError) as exec_info:
        downloader.download("C8763")
    assert exec_info.match("curl_command_not_found")
