from pydantic import BaseModel
from .enums import AuthenticationChallengeType
from typing import Optional


class AuthenticationChallenge(BaseModel):
    type: AuthenticationChallengeType
    fingerprint_url: Optional[str]
    fingerprint_data: Optional[dict]
    acs_url: Optional[str]
