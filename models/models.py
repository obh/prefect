from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict


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





