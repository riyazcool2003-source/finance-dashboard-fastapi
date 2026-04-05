from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


# signup request
class UserCreate(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=72
    )

    role: Optional[str] = "analyst"

    # allowed roles:
    # viewer
    # analyst
    # admin


# response after signup
class UserResponse(BaseModel):

    id: int

    name: str

    email: EmailStr

    role: str

    created_at: datetime


    class Config:

        from_attributes = True


# login request
class UserLogin(BaseModel):

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=72
    )


# JWT response
class Token(BaseModel):

    access_token: str

    token_type: str = "bearer"