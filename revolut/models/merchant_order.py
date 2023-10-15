from pydantic import BaseModel
from typing import Optional


class MerchantOrder(BaseModel):
    url: Optional[str] = None
    reference: Optional[str] = None
