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

_registered_curl_commands[
    "00713"
] = r"""
curl 'https://api.yuantafunds.com/ectranslation/api/trans?APIType=EC2API&AppName=FundWeb&PageName=%2Fmyfund%2Fdividend&Device=4&DeviceId=cbe260a5-df5f-4a3e-a2fe-458b27c8b8e3&FuncId=FundDividend&FundId=1164&FundType=ETF' \
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

_registered_curl_commands[
    "006208"
] = r"""
curl 'https://www.fubon.com/asset-management/fund/info/Json/FundDividendData' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Cookie: TS01c07e83=01773febeb464efd39bbf51892ab09f6acaeef0092f9018f85bdc99857f0af8ac66382f52b79853740e3b893e6363770a6282df6bb; cookie_vix=Y; _ga=GA1.1.616790753.1710172915; cookie_data=Accepted; _ga_NVMW7YS5X1=GS1.1.1710172915.1.1.1710173017.60.0.0; TSd72ffa05027=087a24dea5ab20009ed699650fac2ed8cbdc63f5aebce67bcc20828af7fd047e6ddc55b8d1fed24e08a6bd0468113000c7a0da5409a44924c81a7d27b8435e15ab26f7cf274f0bdd886c8ef2f61a34c5ea52c9956a88d6ec8ef65a2988f91d73' \
  -H 'Origin: https://www.fubon.com' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://www.fubon.com/asset-management/fund/info/dividends?Fd=40' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw 'Fd=40&sDate=2023%2F03%2F12&eDate=2026%2F03%2F12'
"""  # TODO hardcode the end date to 2026


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


def _parser_fubon(stock_number: str, text: str):
    from bs4 import BeautifulSoup
    from stock_info.downloader import Result

    soup = BeautifulSoup(text, "html.parser")
    rows = soup.select("tr")
    lines = []
    for row in rows:
        lines.append([x.text for x in row.select("td")])
    lines = lines[:2]

    data = dict()
    for x in range(len(lines[0])):
        data[lines[0][x]] = lines[1][x]

    # sample_data = {
    #     "年化配息率(%)": "2.28",
    #     "收益分配發放日": "2023/12/12",
    #     "收益分配評價日": "2023/10/31",
    #     "收益分配除息日": "2023/11/16",
    #     "每單位分配金額(元)": "0.8610",
    #     "當期含息報酬率(%)": "0.83",
    #     "當次配息率(%)": "1.14",
    #     "配息年月": "2023/10",
    # }

    return Result(
        success=True,
        stock_number=stock_number,
        dividend=float(data["每單位分配金額(元)"]),
        exDividendDate=data["收益分配除息日"],
        dividendPaymentDate=data["收益分配發放日"],
    )


_registered_parsers["0056"] = _parser_yuantafunds
_registered_parsers["00713"] = _parser_yuantafunds
_registered_parsers["006208"] = _parser_fubon


def find_parser(stock_number: str) -> Callable[[str, str], Any]:
    return _registered_parsers.get(stock_number)
