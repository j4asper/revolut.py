from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .payment_method import PaymentMethod
from .fee import Fee
from .authentication_challenge import AuthenticationChallenge
from .address import Address
from .enums import State, DeclineReason, RiskLevel


class Payment(BaseModel):
    id: str
    state: State
    decline_reason: Optional[DeclineReason]
    bank_message: Optional[str]
    created_at: datetime
    updated_at: datetime
    token: Optional[str]
    amount: int
    currency: str
    settled_amount: Optional[int]
    settled_currency: Optional[str]
    payment_method: Optional[PaymentMethod]
    authentication_challenge: Optional[AuthenticationChallenge]
    billing_address: Optional[Address]
    risk_level = Optional[RiskLevel]
    fees: list[Fee]
