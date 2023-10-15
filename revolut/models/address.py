from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    street_line_1: Optional[str] = None
    street_line_2: Optional[str] = None
    region: Optional[str] = None
    city: Optional[str] = None
    country_code: str
    postcode: str
