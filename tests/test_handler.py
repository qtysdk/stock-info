from stock_info.downloader import Downloader


def test_handler_00878(downloader: Downloader):
    import stock_info.handler

    # patch cached downloader
    stock_info.handler.downloader = downloader
    assert stock_info.handler.downloader.enable_fake is True

    result = stock_info.handler.callback(dict(stock_number="00878"), None)
    assert result == {
        "result": {
            "dividend": 0.4,
            "dividend_date": "2024/02/27",
            "dividend_yield": 1.82,
            "meeting_date": None,
            "payment_date": "2024/03/25",
            "stock_number": "00878",
            "success": True,
        },
        "version": "0.1",
    }
