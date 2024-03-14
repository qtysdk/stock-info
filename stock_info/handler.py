import logging
from dataclasses import asdict
from typing import Dict

from stock_info import Result, get_version
from stock_info.cache import Cache
from stock_info.downloader import Downloader, build_failed_result


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

downloader = Downloader()
cache = Cache()


def build_lambda_result(result: Result, stack_info: str = None):
    if stack_info is not None:
        return dict(version=get_version(), result=asdict(result), stack_info=stack_info)

    return dict(version=get_version(), result=asdict(result))


def callback(event, context):
    if not isinstance(event, Dict):
        return build_lambda_result(build_failed_result("0000"))

    stock_number = event.get("stock_number")
    if not stock_number:
        return build_lambda_result(build_failed_result("0000"))

    try:
        return build_lambda_result(download_or_get_from_cache(stock_number))
    except BaseException as e:
        return build_lambda_result(build_failed_result(stock_number), str(e))


def download_or_get_from_cache(stock_number) -> Result:
    cached: Dict = cache.get_item(stock_number)
    if cached:
        logger.info(f"get {stock_number} from cached")
        try:
            return Result(**cached)
        except BaseException as e:
            # delete invalid data from cache
            cache.delete_item(stock_number)

    result = downloader.download(stock_number)
    if result is not None and result.success:
        cache.put_item(asdict(result))
    return result
