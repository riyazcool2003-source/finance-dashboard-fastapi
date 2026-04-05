from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
    DateTime,
    Boolean,
    Index
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.core.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String,
        nullable=False
    )

    role = Column(
        String(20),
        default="analyst",
        index=True
    )

    # extra improvement
    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    transactions = relationship(

        "Transaction",

        back_populates="user",

        cascade="all, delete"
    )


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(150),
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False,
        index=True
    )

    type = Column(
        String(20),
        nullable=False,
        index=True
    )

    category = Column(
        String(50),
        index=True
    )

    date = Column(
        Date,
        index=True
    )

    notes = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    user = relationship(

        "User",

        back_populates="transactions"
    )


# helpful indexes for filtering performance
Index("idx_user_date", Transaction.user_id, Transaction.date)