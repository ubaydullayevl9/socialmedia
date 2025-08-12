from pydantic import BaseModel
from typing import Optional


class UserPostCreate(BaseModel):
    user_id: int
    main_text: Optional[str] = None


class UserPostUpdate(BaseModel):
    main_text: Optional[str] = None


class UserPostRead(BaseModel):
    id: int
    user_id: int
    main_text: Optional[str] = None

