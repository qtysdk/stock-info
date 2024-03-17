## Stock info

This project is a mini-project designed to collect stock information from listed companies in Taiwan, focusing primarily
on the schedule of stock dividends and distributions. It utilizes a serverless approach, providing functions for use by
other services.

## Usage

Invoke the function and get the information

```sh
aws lambda invoke \
  --function-name stock-info-2024 \
  --cli-binary-format raw-in-base64-out \
  --payload '{"stock_number":"0056"}' \
  --profile local-dev \
  output.json
```

```json
{
  "version": "0.1.10",
  "result": {
    "success": true,
    "stock_number": "0056",
    "dividend": 0.7,
    "dividend_date": "2024/01/17",
    "payment_date": "2024/02/21",
    "meeting_date": null,
    "dividend_yield": 1.89
  }
}
```

### result 欄位說明

| 欄位名稱           | 欄位說明             | 內容範例       |
|----------------|------------------|------------|
| success        | 查詢是否成功           | true       |
| stock_number   | 股票代號             | 0056       |
| dividend       | 股息               | 0.7        |
| dividend_date  | 除息日              | 2024/01/17 |
| payment_date   | 發放股息日            | 2024/02/21 |
| meeting_date   | 股東會日期（若無則為 null） | null       |
| dividend_yield | 股息殖利率            | 1.89       |

* success 為 `true` 時，其它值才有意義。當為 `false` 時，請忽略其它欄位內容。