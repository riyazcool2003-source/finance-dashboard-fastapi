from sqlalchemy.orm import Session

from app.models.models import Transaction


# CREATE
def create_transaction(
    db: Session,
    data,
    user_id: int
):

    transaction = Transaction(

        title=data.title,

        amount=data.amount,

        type=data.type,

        category=data.category,

        date=data.date,

        user_id=user_id
    )


    db.add(transaction)

    db.commit()

    db.refresh(transaction)


    return transaction


# READ
def get_transactions(
    db: Session,
    user_id: int
):

    return db.query(Transaction).filter(

        Transaction.user_id == user_id

    ).all()


# UPDATE
def update_transaction(
    db: Session,
    transaction_id: int,
    data,
    user_id: int
):

    transaction = db.query(Transaction).filter(

        Transaction.id == transaction_id,

        Transaction.user_id == user_id

    ).first()


    if transaction:

        transaction.title = data.title

        transaction.amount = data.amount

        transaction.type = data.type

        transaction.category = data.category

        transaction.date = data.date


        db.commit()

        db.refresh(transaction)


    return transaction


# DELETE
def delete_transaction(
    db: Session,
    transaction_id: int,
    user_id: int
):

    transaction = db.query(Transaction).filter(

        Transaction.id == transaction_id,

        Transaction.user_id == user_id

    ).first()


    if transaction:

        db.delete(transaction)

        db.commit()


    return transaction