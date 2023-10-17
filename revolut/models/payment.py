from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .payment_method import PaymentMethod
from .fee import Fee
from .authentication_challenge import AuthenticationChallenge
from .address import Address

from .enums import (
    State,
    DeclineReason,
    RiskLevel,
    Currency
)


class Payment(BaseModel):
    id: str
    state: State
    decline_reason: Optional[DeclineReason] = None
    bank_message: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    token: Optional[str] = None
    amount: int
    currency: Optional[Currency] = None
    settled_amount: Optional[int] = None
    settled_currency: Optional[Currency] = None
    payment_method: Optional[PaymentMethod] = None
    authentication_challenge: Optional[AuthenticationChallenge] = None
    billing_address: Optional[Address] = None
    risk_level: Optional[RiskLevel] = None
    fees: Optional[List[Fee]] = None
