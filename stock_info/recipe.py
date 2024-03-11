import json
from typing import Any, Callable, Dict

_registered_curl_commands = dict()
_registered_parsers: Dict[str, Callable[[str, str], Any]] = dict()


_registered_curl_commands[
    "0056"
] = r"""
curl 'https://api.yuantafunds.com/ectranslation/api/trans?APIType=EC2API&AppName=FundWeb&PageName=%2Fmyfund%2Fdividend&Device=4&DeviceId=cbe260a5-df5f-4a3e-a2fe-458b27c8b8e3&FuncId=FundDividend&FundId=1084&FundType=ETF' \
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


def find_request_template(stock_number: str) -> str:
    return _registered_curl_commands.get(stock_number)


def _parser_yuantafunds(stock_number: str, text: str):
    from stock_info.downloader import Result

    data = json.loads(text)
    data = data["Data"]["Data"][0]

    return Result(
        success=True,
        stock_number=stock_number,
        dividend=data["DIVIDEN_PER_UNIT"],
        exDividendDate=data["SHARE_DATE"],
        dividendPaymentDate=data["PAY_DATE"],
    )


_registered_parsers["0056"] = _parser_yuantafunds


def find_parser(stock_number: str) -> Callable[[str, str], Any]:
    return _registered_parsers.get(stock_number)
