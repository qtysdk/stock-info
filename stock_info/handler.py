from dataclasses import asdict, dataclass
from typing import Dict

from stock_info import get_version
from stock_info.downloader import Downloader, Result, build_failed_result

dl = Downloader()


def build_lambda_result(result: Result):
    return dict(version=get_version(), result=asdict(result))


def callback(event, context):
    if not isinstance(event, Dict):
        return build_lambda_result(build_failed_result("0000"))

    stock_number = event.get("stock_number")
    if not stock_number:
        return build_lambda_result(build_failed_result("0000"))

    return build_lambda_result(dl.download(stock_number))
