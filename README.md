## Stock info

This project is a mini-project designed to collect stock information from listed companies in Taiwan, focusing primarily on the schedule of stock dividends and distributions. It utilizes a serverless approach, providing functions for use by other services.

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
  "version": "0.1.6",
  "result": {
    "success": true,
    "stock_number": "0056",
    "dividend": 0.7,
    "exDividendDate": "2024/01/17",
    "dividendPaymentDate": "2024/02/21",
    "meetingDate": null,
    "dividend_yield": 1.89
  }
}
```