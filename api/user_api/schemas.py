from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    surname: str
    username: Optional[str] = None
    email: str
    password: str
    birthday: Optional[str] = None
    city: Optional[str] = None

