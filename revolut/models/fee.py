from pydantic import BaseModel
from typing import Optional
from .enums import FeeType


class Fee(BaseModel):
    type: Optional[FeeType]
    amount: Optional[int]
    currency: Optional[str]
