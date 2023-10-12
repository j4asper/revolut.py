from pydantic import BaseModel
from typing import Optional


class ShippingAddress(BaseModel):
    street_line_1: Optional[str]
    street_line_2: Optional[str]
    region: Optional[str]
    city: Optional[str]
    country_code: str
    postcode: str
