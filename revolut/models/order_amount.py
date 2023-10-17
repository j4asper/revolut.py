from pydantic import BaseModel
from .enums import Currency


class OrderAmount(BaseModel):
    value: int
    currency: Currency
