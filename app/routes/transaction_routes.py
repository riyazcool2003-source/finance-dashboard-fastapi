from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.transaction_schema import (
    TransactionCreate,
    TransactionResponse
)

from app.services.transaction_service import (
    create_transaction,
    get_transactions,
    update_transaction,
    delete_transaction
)

from app.core.security import get_current_user


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


# viewer cannot create
@router.post("", response_model=TransactionResponse)
def create(
    data: TransactionCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    if current_user.role not in ["analyst", "admin"]:

        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    return create_transaction(
        db,
        data,
        current_user.id
    )


# all roles can view
@router.get("", response_model=list[TransactionResponse])
def get_all(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return get_transactions(
        db,
        current_user.id
    )


# analyst + admin can update
@router.put("/{id}", response_model=TransactionResponse)
def update(
    id: int,
    data: TransactionCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    if current_user.role not in ["analyst", "admin"]:

        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    return update_transaction(
        db,
        id,
        data,
        current_user.id
    )


# only admin can delete
@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin only"
        )

    return delete_transaction(
        db,
        id,
        current_user.id
    )