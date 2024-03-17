## Stock info

This project is a focused initiative aimed at gathering stock information from publicly traded companies in Taiwan. It zeroes in on the critical aspects of stock dividends and distributions schedules, offering valuable insights for stakeholders. By adopting a serverless architecture, the project ensures scalability and flexibility, enabling seamless integration and utilization by various services.

這個專案是一項專注於搜集台灣上市公司股票資訊的計劃，主要集中於股息和分配時間表的關鍵細節。透過提供這些重要資訊，專案為相關利益者提供了寶貴的洞見。採用無伺服器架構確保了專案的可擴展性和靈活性，使其能夠輕鬆整合並被各種服務使用。

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