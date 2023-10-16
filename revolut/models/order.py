from pydantic import BaseModel
from typing import Optional
from .customer import CustomerModel
from .address import Address
from .payment import Payment
from .merchant_order import MerchantOrder
from .upcoming_payment import UpcomingPayment

from datetime import (
    datetime,
    timedelta
)

from .enums import (
    OrderType,
    State,
    CaptureMode,
    Currency,
    EnforceChallenge
)


class OrderModel(BaseModel):
    amount: int
    currency: Currency
    id: Optional[str] = None
    token: Optional[str] = None
    type: Optional[OrderType] = None
    state: Optional[State] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    description: Optional[str] = None
    capture_mode: Optional[CaptureMode] = None
    enforce_challenge: Optional[EnforceChallenge] = None
    cancel_authorised_after: Optional[timedelta] = None
    outstanding_amount: Optional[int] = None
    refunded_amount: Optional[int] = None
    settlement_currency: Optional[Currency] = None
    customer: Optional[CustomerModel] = None
    shipping_address: Optional[Address] = None
    payments: Optional[list[Payment]] = None
    location_id: Optional[str] = None
    metadata: Optional[dict] = None
    industry_data: Optional[dict] = None
    merchant_order_data: Optional[MerchantOrder] = None
    upcoming_payment_data: Optional[UpcomingPayment] = None
    checkout_url: Optional[str] = None
