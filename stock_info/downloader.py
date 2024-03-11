import json
import os
import logging
import re
from dataclasses import dataclass

import requests

logger = logging.getLogger(__name__)


@dataclass
class Result:
    success: bool
    stock_number: str
    dividend: float
    exDividendDate: str
    dividendPaymentDate: str


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

    def download(self, key: str):
        text = self.http_request_for(key)
        if text:
            return self.parse_for(key, text)

        return build_failed_result(key)

    def http_request_for(self, key):
        # TODO fix the hardcode 0056 (1084)

        curl_command = r"""
curl 'https://api.yuantafunds.com/ectranslation/api/trans?APIType=EC2API&AppName=FundWeb&PageName=%2Fmyfund%2Fdividend&Device=4&DeviceId=cbe260a5-df5f-4a3e-a2fe-458b27c8b8e3&FuncId=FundDividend&FundId=1084&SDate=20240101&EDate=20241231&FundType=ETF' \
  -H 'authority: api.yuantafunds.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'origin: https://www.yuantafunds.com' \
  -H 'pragma: no-cache' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        """

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

        return requests.get(url, headers=headers).text

    def parse_for(self, key: str, text: str):
        # TODO fix the ignored key
        data = json.loads(text)
        data = data["Data"]["Data"][0]

        return Result(
            success=True,
            stock_number=key,
            dividend=data["DIVIDEN_PER_UNIT"],
            exDividendDate=data["SHARE_DATE"],
            dividendPaymentDate=data["PAY_DATE"],
        )
