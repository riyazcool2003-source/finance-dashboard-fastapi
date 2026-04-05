from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm

from app.core.database import get_db

from app.schemas.auth_schema import TokenResponse

from app.services.auth_service import (
    authenticate_user,
    create_access_token
)

router = APIRouter(
    tags=["Auth"]
)


@router.post("/login", response_model=TokenResponse)
def login(

    form_data: OAuth2PasswordRequestForm = Depends(),

    db: Session = Depends(get_db)

):

    # username field is used as email
    user = authenticate_user(

        db,

        form_data.username,

        form_data.password
    )

    if not user:

        raise HTTPException(

            status_code=401,

            detail="Invalid email or password"
        )

    token = create_access_token(

        {

            "user_id": user.id,

            "role": user.role

        }

    )

    return {

        "access_token": token,

        "token_type": "bearer"

    }