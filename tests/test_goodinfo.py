from stock_info import Result
from stock_info.downloader import Downloader


def test_fetch_2412(downloader: Downloader):
    result = downloader.download("2412")
    assert result == Result(
        success=True,
        stock_number="2412",
        dividend=4.76,
        dividend_date="2024/07/04",
        payment_date="2024/08/08",
        meeting_date="2024/05/31",
        dividend_yield=3.86,
    )


def test_fetch_2330(downloader: Downloader):
    result = downloader.download("2330")
    assert result == Result(
        success=True,
        stock_number="2330",
        dividend=4.5,
        dividend_date="",
        payment_date="",
        meeting_date="",
        dividend_yield=0.41,
    )


def test_fetch_2887(downloader: Downloader):
    result = downloader.download("2887")
    assert result == Result(
        success=True,
        stock_number="2887",
        dividend=0.6,
        dividend_date="2024/08/06",
        payment_date="2024/08/29",
        meeting_date="2024/06/14",
        dividend_yield=3.31,
    )
