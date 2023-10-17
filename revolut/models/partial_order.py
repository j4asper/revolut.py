from pydantic import BaseModel
from typing import Optional
from .address import Address
from .order_amount import OrderAmount
from datetime import datetime

from .enums import (
    OrderType,
    State,
    CaptureMode,
    Currency,
)


class PartialOrderModel(BaseModel):
    id: Optional[str] = None
    type: Optional[OrderType] = None
    order_amount: Optional[OrderAmount] = None
    customer_id: Optional[str] = None
    merchant_order_ext_ref: Optional[str] = None
    state: Optional[State] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    description: Optional[str] = None
    capture_mode: Optional[CaptureMode] = None
    settlement_currency: Optional[Currency] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    shipping_address: Optional[Address] = None
    order_outstanding_amount: Optional[OrderAmount] = None
