from pydantic import BaseModel
from .enums import State


class ThreeDS(BaseModel):
    state: State
    version: int
