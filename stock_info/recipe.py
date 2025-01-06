import json
import re
from typing import Any, Callable, Dict, List

from bs4 import BeautifulSoup

from stock_info import DividendYield, Result

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
curl 'https://www.capitalfund.com.tw/CFWeb/api/etf/dividendDataHistory' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'cookie: visid_incap_2932320=/PREwmg+S4G+Dl6k4zT/9PfvIWYAAAAAQUIPAAAAAAClAo09etWBe/FBrvXHT1FT; nlbi_2932320=XF0eQ+Ari0PMhz/zOwe3HgAAAACv4clnVObzvsenJ/NZTd/M; _gcl_au=1.1.514858647.1713500222; _gid=GA1.3.1086922653.1713500222; tr_uid=mSSMJa-P4y7NegmSDRlXvQ; oid=%257B%2522oid%2522%253A%2522f66a6492-04d5-11ee-a4b8-0242ac130002%2522%252C%2522_oldoid%2522%253A%2522673d3c9d-2896-11ee-ac30-0242ac130002%2522%252C%2522ts%2522%253A-62135596800%252C%2522v%2522%253A%252220201118%2522%257D; incap_ses_937_2932320=tP9KE8LB11r960fFjeQADbxsImYAAAAA0OcpsERCzg5LXF3CNbklRQ==; _gat_UA-64516633-1=1; _ga=GA1.1.1583655619.1713500222; _ga_VN37CHZ283=GS1.1.1713532093.3.1.1713532108.45.0.0; _uetsid=ac209320fe0311ee99d6dd7a330d747f; _uetvid=04096340ad4711ee8f8ee58100ecc449' \
  -H 'origin: https://www.capitalfund.com.tw' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.capitalfund.com.tw/etf/product/detail/195/interest' \
  -H 'sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
  --data-raw '{"searchType":3,"interestCycle":"","fundid":"195"}'
"""

date_00929_start, date_00929_end = dates_between_today_and_last_year()

_registered_curl_commands[
    "00929"
] = rf"""
curl 'https://www.fhtrust.com.tw/api/fundDividend?m=fund&fundID=ETF21&sDate={date_00929_start}&eDate={date_00929_end}&dateType=divDate&ec001=3'
"""


def create_goodinfo_template(stock_number: str):
    # 股利政策
    if "_yield" in stock_number:
        stock_id = stock_number.replace("_yield", "")
        return rf"""
curl 'https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID={stock_id}' \
  -H 'authority: goodinfo.tw' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'cookie: _ga=GA1.1.1493109859.1655977160; CLIENT%5FID=20230908075958144%5F118%2E160%2E128%2E120; IS_TOUCH_DEVICE=F; SCREEN_SIZE=WIDTH=1920&HEIGHT=1080; TW_STOCK_BROWSE_LIST=2412%7C2538; _ga_0LP5MLQS7E=GS1.1.1710387987.7.1.1710388043.4.0.0' \
  -H 'pragma: no-cache' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        """

    # 除權息日程
    return rf"""
curl 'https://goodinfo.tw/tw/StockDividendSchedule.asp?STOCK_ID={stock_number}' \
  -H 'authority: goodinfo.tw' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cache-control: no-cache' \
  -H 'cookie: CLIENT%5FID=20240217232658953%5F118%2E167%2E157%2E141; _ga=GA1.1.999731202.1708183620; IS_TOUCH_DEVICE=F; SCREEN_SIZE=WIDTH=1920&HEIGHT=1080; TW_STOCK_BROWSE_LIST=2412%7C00878; _ga_0LP5MLQS7E=GS1.1.1710296364.4.1.1710298193.60.0.0' \
  -H 'pragma: no-cache' \
  -H 'referer: https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID={stock_number}' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    """


def find_request_template(stock_number: str) -> str:
    if "_yield" in stock_number:
        return create_goodinfo_template(stock_number)

    template = _registered_curl_commands.get(stock_number)
    if template is None:
        if re.match(r"[0-9]+", stock_number):
            return create_goodinfo_template(stock_number)
    return template


def _parser_yuantafunds(stock_number: str, text: str):
    data = json.loads(text)
    data = data["Data"]["Data"][0]

    return Result(
        success=True,
        stock_number=stock_number,
        dividend=data["DIVIDEN_PER_UNIT"],
        dividend_date=data["SHARE_DATE"],
        payment_date=data["PAY_DATE"],
    )


def _parser_fubon(stock_number: str, text: str):

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
        dividend_date=data["收益分配除息日"],
        payment_date=data["收益分配發放日"],
    )


def _parser_cathaysite(stock_number: str, text: str):
    data = json.loads(text)
    data = data["result"]["fundAllotInfoList"][0]
    return Result(
        success=True,
        stock_number=stock_number,
        dividend=data["allotMoney"],
        dividend_date=data["transDate"],
        payment_date=data["lendingDate"],
    )


def _parser_capitalfund(stock_number: str, text: str):
    data = json.loads(text)
    data = data["data"][0]
    return Result(
        success=True,
        stock_number=stock_number,
        dividend=float(data["amt"]),
        dividend_date=data["interestDate"],
        payment_date=data["assignDate"],
    )


def _parser_fhtrust(stock_number: str, text: str):
    data = json.loads(text)
    data = data["result"][0]["dividend"][0]
    return Result(
        success=True,
        stock_number=stock_number,
        dividend=float(data["mDiv"]),
        dividend_date=data["divDate"],
        payment_date=data["grantDate"],
    )


_registered_parsers["0056"] = _parser_yuantafunds
_registered_parsers["00713"] = _parser_yuantafunds
_registered_parsers["006208"] = _parser_fubon
_registered_parsers["00878"] = _parser_cathaysite
_registered_parsers["00919"] = _parser_capitalfund
_registered_parsers["00929"] = _parser_fhtrust


def _parser_goodinfo_StockDividendPolicy(stock_number: str, text: str):
    soup = BeautifulSoup(text, "html.parser")
    table = soup.select_one("#tblDetail")
    rows = table.select("tr")
    row_texts = [[td.text for td in row] for row in rows]
    row_texts = [r for r in row_texts if r and len(r) == 24]

    rate = None

    try:
        rate = float(row_texts[0][14])
    except:
        pass

    if rate is None:
        try:
            rate = float(row_texts[1][14])
        except:
            pass

    return DividendYield(rate=rate)


def _parser_goodinfo_StockDividendSchedule(stock_number: str, text: str):
    soup = BeautifulSoup(text, "html.parser")
    table = soup.select_one("#tblDetail")
    rows = table.select("tr")
    row_texts = [[td.text for td in row] for row in rows]
    row_texts = [r for r in row_texts if r and r[0].strip()]

    def to_dict(data: List) -> Dict:
        # ensure the record having 19 fields
        if len(data) != 19:
            return None

        def fix_date(date_str: str) -> str:
            import datetime

            if not date_str.strip():
                return ""

            # remove special and non-date info
            # eg. 24/04/11即將發放
            # eg. 24/04/11即狀除息
            date_str = re.sub(r"[^0-9/]", "", date_str)
            date_obj = datetime.datetime.strptime(date_str, "%y/%m/%d")
            return date_obj.strftime("%Y/%m/%d")

        meetingDate = fix_date(data[2])
        exDividendDate = fix_date(data[3])
        dividendPaymentDate = fix_date(data[7])

        try:
            # 只取現金股利，不要用合理股利。
            dividend = float(data[14])
        except:
            dividend = None

        return dict(
            meetingDate=meetingDate,
            exDividend=exDividendDate,
            dividend=dividend,
            dividendPaymentDate=dividendPaymentDate,
        )

    row_texts = [to_dict(r) for r in row_texts]
    row_texts = [r for r in row_texts if r]
    data = row_texts[0]

    return Result(
        success=True,
        stock_number=stock_number,
        dividend=data["dividend"],
        dividend_date=data["exDividend"],
        payment_date=data["dividendPaymentDate"],
        meeting_date=data["meetingDate"],
    )


def _parser_noop(stock_number: str, text: str):

    if "https://goodinfo.tw/tw/StockDividendSchedule.asp" in text:
        return _parser_goodinfo_StockDividendSchedule(stock_number, text)

    if "https://goodinfo.tw/tw/StockDividendPolicy.asp" in text:
        return _parser_goodinfo_StockDividendPolicy(stock_number, text)

    return Result(
        success=True,
        stock_number=stock_number,
        dividend=0,
        dividend_date="noop",
        payment_date="noop",
    )


def find_parser(stock_number: str) -> Callable[[str, str], Any]:

    return _registered_parsers.get(stock_number, _parser_noop)
