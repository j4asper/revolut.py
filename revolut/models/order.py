from pydantic import BaseModel
from typing import Optional
from .customer import CustomerModel
from .address import Address
from .payment import Payment
from .merchant_order import MerchantOrder
from .upcoming_payment import UpcomingPayment
from datetime import datetime, timedelta
from .enums import OrderType, State, CaptureMode, Currency


class OrderModel(BaseModel):
    id: Optional[str]
    token: Optional[str]
    type: Optional[OrderType]
    state: Optional[State]
    created_at: datetime
    updated_at: datetime
    description: Optional[str]
    capture_mode: Optional[CaptureMode]
    cancel_authorised_after: Optional[timedelta]
    amount: int
    outstanding_amount: Optional[int]
    refunded_amount: Optional[int]
    currency: Currency
    settlement_currency: Optional[Currency]
    customer: Optional[CustomerModel]
    shipping_address: Optional[Address]
    payments: list[Payment]
    location_id: Optional[str]
    metadata: Optional[dict]
    industry_data: Optional[dict]
    merchant_order_data: Optional[MerchantOrder]
    upcoming_payment_data: Optional[UpcomingPayment]
    checkout_url: Optional[str]
