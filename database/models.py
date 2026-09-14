from datetime import date

from sqlalchemy import (
    Boolean,
    Date,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    author: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    isbn: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    borrowings: Mapped[list["BorrowingModel"]] = relationship(
        back_populates="book"
    )


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    user_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    borrowings: Mapped[list["BorrowingModel"]] = relationship(
        back_populates="user"
    )


class BorrowingModel(Base):
    __tablename__ = "borrowings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id"),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    borrowed_at: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    due_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    returned_at: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    book: Mapped["BookModel"] = relationship(
        back_populates="borrowings"
    )

    user: Mapped["UserModel"] = relationship(
        back_populates="borrowings"
    )