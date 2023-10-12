from pydantic import BaseModel
from datetime import datetime


class UpcomingPayment(BaseModel):
    date: datetime
    payment_method_id: str
