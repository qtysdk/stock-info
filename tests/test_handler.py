from stock_info.downloader import Downloader


def test_handler_00878(downloader: Downloader):
    import stock_info.handler

    # patch cached downloader
    stock_info.handler.downloader = downloader
    assert stock_info.handler.downloader.enable_fake is True

    result = stock_info.handler.callback(dict(stock_number="00878"), None)
    assert result == {
        "result": {
            "dividend": 0.55,
            "dividend_date": "2024/08/16",
            "dividend_yield": 6.44,
            "meeting_date": None,
            "payment_date": "2024/09/11",
            "stock_number": "00878",
            "success": True,
        },
        "version": "0.1",
    }
