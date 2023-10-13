from pydantic import BaseModel
from typing import Optional
from .checks import Checks

from .enums import (
    PaymentType,
    CardBrand,
    Funding
)


class PaymentMethod(BaseModel):
    id: Optional[str]
    type: PaymentType
    card_brand: Optional[CardBrand]
    funding: Optional[Funding]
    card_country_code: Optional[str]
    card_bin: Optional[str]
    card_last_four: Optional[str]
    card_expiry: Optional[str]
    cardholder_name: Optional[str]
    checks: Optional[Checks]
