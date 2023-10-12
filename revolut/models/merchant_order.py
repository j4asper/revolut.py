from pydantic import BaseModel
from typing import Optional


class MerchantOrder(BaseModel):
    url: Optional[str]
    reference: Optional[str]
