from pydantic import BaseModel
from .enums import AuthenticationChallengeType
from typing import Optional


class AuthenticationChallenge(BaseModel):
    type: AuthenticationChallengeType
    fingerprint_url: Optional[str] = None
    fingerprint_data: Optional[dict] = None
    acs_url: Optional[str] = None
