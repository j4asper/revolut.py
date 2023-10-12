from pydantic import BaseModel
from typing import Optional
from .three_ds import ThreeDS
from .enums import VerificationResult


class Checks(BaseModel):
    three_ds: Optional[ThreeDS]
    cvv_verification: Optional[VerificationResult]
    address: Optional[VerificationResult]
    postcode: Optional[VerificationResult]
    cardholder: Optional[VerificationResult]
