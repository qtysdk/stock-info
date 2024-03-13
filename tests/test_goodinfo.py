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
    )
