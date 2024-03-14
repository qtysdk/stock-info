import os
from dataclasses import dataclass
from typing import Optional


def get_version():
    version_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "VERSION"))
    with open(version_file) as fh:
        version = fh.read().strip()
        return version


@dataclass
class Result:
    success: bool
    stock_number: str
    dividend: float
    dividend_date: str
    payment_date: str
    meeting_date: Optional[str] = None
    dividend_yield: Optional[float] = None


@dataclass
class DividendYield:
    rate: float
