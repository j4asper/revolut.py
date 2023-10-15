from pydantic import BaseModel
from typing import Optional
from .checks import Checks

from .enums import (
    PaymentType,
    CardBrand,
    Funding
)


class PaymentMethod(BaseModel):
    id: Optional[str] = None
    type: PaymentType
    card_brand: Optional[CardBrand] = None
    funding: Optional[Funding] = None
    card_country_code: Optional[str] = None
    card_bin: Optional[str] = None
    card_last_four: Optional[str] = None
    card_expiry: Optional[str] = None
    cardholder_name: Optional[str] = None
    checks: Optional[Checks] = None
