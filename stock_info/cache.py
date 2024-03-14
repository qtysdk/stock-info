import json
import os
import time
from copy import deepcopy
from typing import Dict, Optional

import boto3


class Cache:

    def __init__(self):
        cache_table = os.environ.get("CACHE_TABLE_NAME")
        if not cache_table:
            raise ValueError("CACHE_TABLE_NAME environment variable was not set.")

        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(cache_table)
        self.table = table

    def put_item(self, data: Dict, ttl: int = 0) -> Dict:
        ttl_value = int(time.time()) + 86400
        if ttl != 0:
            ttl_value = ttl

        self.table.put_item(
            Item={
                "stock_number": data["stock_number"],
                "ttl": ttl_value,
                "data": json.dumps(data),
            }
        )
        return data

    def get_item(self, stock_number: str) -> Optional[Dict]:
        response = self.table.get_item(Key={"stock_number": stock_number})

        item = response.get("Item")
        if item is None:
            return None

        return json.loads(item["data"])

    def delete_item(self, stock_number: str):
        response = self.table.delete_item(Key={"stock_number": stock_number})
        return response
