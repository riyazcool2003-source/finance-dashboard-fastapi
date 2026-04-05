from pydantic import BaseModel, Field
from datetime import date as DateType
from typing import Optional


# request schema (used when creating transaction)
class TransactionCreate(BaseModel):

    title: str = Field(
        min_length=2,
        max_length=100
    )

    amount: float = Field(
        gt=0
    )

    type: str = Field(
        pattern="^(income|expense)$"
    )

    category: Optional[str] = None

    date: Optional[DateType] = None


# response schema (returned from API)
class TransactionResponse(BaseModel):

    id: int

    title: str

    amount: float

    type: str

    category: Optional[str]

    date: Optional[DateType]


    class Config:

        from_attributes = True