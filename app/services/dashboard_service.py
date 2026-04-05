from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.models import Transaction


def get_summary(
    db: Session,
    user_id: int
):

    # total income
    total_income = db.query(

        func.sum(Transaction.amount)

    ).filter(

        Transaction.user_id == user_id,

        Transaction.type == "income"

    ).scalar() or 0


    # total expense
    total_expense = db.query(

        func.sum(Transaction.amount)

    ).filter(

        Transaction.user_id == user_id,

        Transaction.type == "expense"

    ).scalar() or 0


    # net balance
    balance = total_income - total_expense


    return {

        "total_income": total_income,

        "total_expense": total_expense,

        "balance": balance
    }