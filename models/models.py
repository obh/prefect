from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict
import json


class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BLOCKED = "blocked"


class Provider(str, Enum):
    Cashfree = "cashfree"
    Razorpay = "razorpay"
    PayU = "payu"
    PayTM = "paytm"


ProviderFields = {
        Provider.Cashfree: ['clientId', 'clientSecret'],
        Provider.Razorpay: ['appId', 'secret']
    }


@dataclass
class CredEntry:
    provider: Provider
    client_id: str
    credentials: Dict[str, str]
    status: Status
    added_on: datetime
    updated_on: datetime


def credentry_from_row(row):
    print(row)
    return CredEntry(
        provider=row['provider'],
        client_id=row['client_id'],
        credentials=json.loads(row['credentials']),
        status=Status(row['status']),
        added_on=row['added_on'],
        updated_on=row['updated_on']
    )



