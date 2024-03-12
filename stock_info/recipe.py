import json
from typing import Any, Callable, Dict

_registered_curl_commands = dict()
_registered_parsers: Dict[str, Callable[[str, str], Any]] = dict()


from datetime import datetime, timedelta


def dates_between_today_and_last_year():
    today = datetime.now()
    one_year_ago = today - timedelta(days=365)
    return one_year_ago.strftime("%Y/%m/%d"), today.strftime("%Y/%m/%d")


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

_registered_curl_commands[
    "00878"
] = r"""
curl 'https://cwapi.cathaysite.com.tw/api/Fund/GetHistoryAllotInfo?fundCode=CN&IsFromBorn=true&StartYear=&EndYear=&CurrentPage=1&PerPageCount=9999' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://www.cathaysite.com.tw' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://www.cathaysite.com.tw/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiIxNDk4MTM0IiwidW5pcXVlX25hbWUiOiIiLCJyb2xlIjoiMCIsIkVDSUQiOiIwIiwibmJmIjoxNzEwMTc1Mjg0LCJleHAiOjE3NzAxNzUyMjQsImlhdCI6MTcxMDE3NTI4NH0.aNhFnHi_rAAIN-jUJCOlFFe2_Vss-NdI3A3JWVl8O1M' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"'
"""  # TODO the jwt token will expire after 2026

_registered_curl_commands[
    "00919"
] = r"""
curl 'https://www.capitalfund.com.tw/CFWeb/api/etf/dividendData3/195' \
  -X 'POST' \
  -H 'authority: www.capitalfund.com.tw' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'content-length: 0' \
  -H 'cookie: visid_incap_2932320=o3BJNXQmTcOpAwG+m9t5fg/B72UAAAAAQUIPAAAAAABv7VIjwkPmMfcBNTKvGWX7; incap_ses_933_2932320=ctHEDDA9zncjkzdLqK/yDA/B72UAAAAAPoOPrCIQb5jgloeueKwKHg==; nlbi_2932320=p3ytGrxDSlxU6wztVMy66wAAAABHmCnyZ1x2BNR7lKTUJzsZ; _gcl_au=1.1.801827870.1710211344; _gid=GA1.3.2087569856.1710211344; tr_uid=vbV6XnVWFioTfDmst6Rb5Q; oid=%257B%2522oid%2522%253A%2522285ab476-e01a-11ee-8d99-0242ac130002%2522%252C%2522_oldoid%2522%253A%2522285ab461-e01a-11ee-8d99-0242ac130002%2522%252C%2522ts%2522%253A-62135596800%252C%2522v%2522%253A%252220201118%2522%257D; _gat_UA-64516633-1=1; _ga=GA1.1.1426833675.1710211344; _ga_VN37CHZ283=GS1.1.1710211344.1.1.1710211495.60.0.0; _uetsid=284ddc60e01a11eeb0f9bb2865f6d61e; _uetvid=284dff20e01a11eea969b9d7f1aefcd0' \
  -H 'origin: https://www.capitalfund.com.tw' \
  -H 'pragma: no-cache' \
  -H 'referer: https://www.capitalfund.com.tw/etf/product/detail/195/interest' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
"""

date_00929_start, date_00929_end = dates_between_today_and_last_year()

_registered_curl_commands[
    "00929"
] = rf"""
curl 'https://www.fhtrust.com.tw/api/fundDividend?m=fund&fundID=ETF21&sDate={date_00929_start}&eDate={date_00929_end}&dateType=divDate&ec001=3'
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


def _parser_cathaysite(stock_number: str, text: str):
    from stock_info.downloader import Result

    data = json.loads(text)
    data = data["result"]["fundAllotInfoList"][0]
    return Result(
        success=True,
        stock_number=stock_number,
        dividend=data["allotMoney"],
        exDividendDate=data["transDate"],
        dividendPaymentDate=data["lendingDate"],
    )


def _parser_capitalfund(stock_number: str, text: str):
    from stock_info.downloader import Result

    data = json.loads(text)
    data = data["data"][0]
    return Result(
        success=True,
        stock_number=stock_number,
        dividend=float(data["amt"]),
        exDividendDate=data["interestDate"],
        dividendPaymentDate=data["assignDate"],
    )


def _parser_fhtrust(stock_number: str, text: str):
    from stock_info.downloader import Result

    data = json.loads(text)
    data = data["result"][0]["dividend"][0]
    return Result(
        success=True,
        stock_number=stock_number,
        dividend=float(data["mDiv"]),
        exDividendDate=data["divDate"],
        dividendPaymentDate=data["grantDate"],
    )


_registered_parsers["0056"] = _parser_yuantafunds
_registered_parsers["00713"] = _parser_yuantafunds
_registered_parsers["006208"] = _parser_fubon
_registered_parsers["00878"] = _parser_cathaysite
_registered_parsers["00919"] = _parser_capitalfund
_registered_parsers["00929"] = _parser_fhtrust


def find_parser(stock_number: str) -> Callable[[str, str], Any]:
    def _parser_noop(stock_number: str, text: str):
        from stock_info.downloader import Result

        return Result(
            success=True,
            stock_number=stock_number,
            dividend=0,
            exDividendDate="noop",
            dividendPaymentDate="noop",
        )

    return _registered_parsers.get(stock_number, _parser_noop)
