from pydantic import BaseModel
from typing import Optional
from .three_ds import ThreeDS
from .enums import VerificationResult


class Checks(BaseModel):
    three_ds: Optional[ThreeDS] = None
    cvv_verification: Optional[VerificationResult] = None
    address: Optional[VerificationResult] = None
    postcode: Optional[VerificationResult] = None
    cardholder: Optional[VerificationResult] = None
