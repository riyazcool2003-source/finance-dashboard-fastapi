from sqlalchemy.orm import Session

from app.models import models

from app.schemas.user_schema import UserCreate

from app.services.auth_service import hash_password


def create_user(
    db: Session,
    user: UserCreate
):

    # check if email already exists
    existing_user = db.query(
        models.User
    ).filter(
        models.User.email == user.email
    ).first()


    if existing_user:

        raise Exception(
            "Email already exists"
        )


    # allowed roles
    allowed_roles = [

        "viewer",

        "analyst",

        "admin"

    ]


    # validate role
    role = user.role


    if role not in allowed_roles:

        role = "analyst"


    # create user
    new_user = models.User(

        name=user.name,

        email=user.email,

        password=hash_password(
            user.password
        ),

        role=role
    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)


    return new_user