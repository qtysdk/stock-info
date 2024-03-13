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
    exDividendDate: str
    dividendPaymentDate: str
    meetingDate: Optional[str] = None
