from pydantic import BaseModel
from typing import Optional

from .enums import (
    FeeType,
    Currency
)


class Fee(BaseModel):
    type: Optional[FeeType] = None
    amount: Optional[int] = None
    currency: Optional[Currency] = None
