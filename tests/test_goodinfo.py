from stock_info import Result
from stock_info.downloader import Downloader


def test_fetch_2412(downloader: Downloader):
    result = downloader.download("2412")
    assert result == Result(
        success=True,
        stock_number="2412",
        dividend=4.758,
        exDividendDate="",
        dividendPaymentDate="",
        meetingDate="2024/05/31",
        dividend_yield=3.95,
    )


def test_fetch_2330(downloader: Downloader):
    result = downloader.download("2330")
    assert result == Result(
        success=True,
        stock_number="2330",
        dividend=3.5,
        exDividendDate="",
        dividendPaymentDate="",
        meetingDate="",
        dividend_yield=1.06,
    )
