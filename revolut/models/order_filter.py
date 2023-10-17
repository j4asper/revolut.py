from pydantic import BaseModel
from typing import Optional
from .enums import State
from datetime import datetime


class OrderFilter(BaseModel):
    created_before: Optional[datetime] = None,
    from_created_date: Optional[datetime] = None,
    to_created_date: Optional[datetime] = None,
    customer_id: Optional[str] = None,
    email: Optional[str] = None,
    merchant_order_ext_ref: Optional[str] = None,
    state: Optional[State] = None,
    limit: Optional[int] = None
