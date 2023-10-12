from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CustomerModel(BaseModel):
    id: str
    full_name: Optional[str]
    business_name: Optional[str]
    phone: Optional[str]
    created_at: datetime
    updated_at: datetime
    email: str
