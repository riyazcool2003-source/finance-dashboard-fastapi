from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.security import get_current_user

from app.services.dashboard_service import get_summary


router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]

)


# all roles can view dashboard
@router.get("/summary")
def summary(

    db: Session = Depends(get_db),

    current_user = Depends(get_current_user)

):

    return get_summary(

        db,

        current_user.id
    )