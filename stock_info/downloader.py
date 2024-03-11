import json
import os
import logging
import re
from dataclasses import dataclass
from typing import Callable, Dict

import requests

from stock_info.recipe import find_parser, find_request_template

logger = logging.getLogger(__name__)


@dataclass
class Result:
    success: bool
    stock_number: str
    dividend: float
    exDividendDate: str
    dividendPaymentDate: str


@dataclass
class RequestParameters:
    url: str
    headers: Dict


def create_request_parameters_from_curl_command(curl_command: str) -> RequestParameters:
    if curl_command is None:
        raise ValueError("curl_command_not_found")
    lines = re.findall(r"(curl|-H) '([^']+)'.*", curl_command)
    url = None
    headers = dict()
    for line in lines:
        data_type, value = line
        if data_type == "curl":
            url = value
        if data_type == "-H":
            parsed = re.findall(r"(^[^:]+): (.+)", value)
            if parsed:
                header_name, header_value = parsed[0]
                headers[header_name] = header_value
    return RequestParameters(url=url, headers=headers)


def build_failed_result(key: str):
    return Result(
        success=False,
        dividend=0.0,
        dividendPaymentDate="",
        exDividendDate="",
        stock_number=key,
    )


class Downloader:

    def __init__(self):
        self.enable_fake = "true" == os.environ.get("FAKE_DOWNLOADER", "false")
        logger.info(f"is-fake-enabled: {self.enable_fake}")

    def download(self, key: str) -> Result:
        text = None
        if self.enable_fake:
            text = self.use_previous_data(key)
        else:
            text = self.http_request_for(key)
        if text:
            parse_func: Callable[[str, str], Result] = find_parser(key)
            return parse_func(key, text)
        return build_failed_result(key)

    def use_previous_data(self, key: str):
        import stock_info
        import pathlib

        test_dir = pathlib.Path(stock_info.__file__).parent.parent / "tests"
        testdata_dir = test_dir / "data"
        testdata_dir.mkdir(exist_ok=True)
        testdata = testdata_dir / f"{key}.data"

        if (
            "true" == os.environ.get("MAKE_NEW_TESTDATA", "false")
            or not testdata.exists()
        ):
            text = self.http_request_for(key)
            with open(testdata, "w") as fh:
                fh.write(text)
            return text

        if testdata.exists():
            logger.warning(f"Load from testdata for {key}")
            with open(testdata, "r") as fh:
                return fh.read()

    def http_request_for(self, stock_number: str):
        params = create_request_parameters_from_curl_command(
            find_request_template(stock_number)
        )
        return requests.get(params.url, headers=params.headers).text
