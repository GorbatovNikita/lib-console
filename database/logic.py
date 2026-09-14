from datetime import date, timedelta

from sqlalchemy import select

from database.decorators import with_session
from database.models import BookModel, BorrowingModel, UserModel


@with_session
def add_book(session, title: str, author: str, isbn: str) -> bool:
    existing_book = session.scalar(
        select(BookModel).where(BookModel.isbn == isbn)
    )

    if existing_book is not None:
        return False

    book = BookModel(
        title=title,
        author=author,
        isbn=isbn,
        available=True
    )

    session.add(book)

    return True


@with_session
def remove_book(session, isbn: str) -> bool:
    book = session.scalar(
        select(BookModel).where(BookModel.isbn == isbn)
    )

    if book is None:
        return False

    if not book.available:
        return False

    session.delete(book)

    return True


@with_session
def search_books(
    session,
    title: str | None = None,
    author: str | None = None,
    isbn: str | None = None
):
    query = select(BookModel)

    if title is not None:
        query = query.where(
            BookModel.title.ilike(f"%{title}%")
        )

    if author is not None:
        query = query.where(
            BookModel.author.ilike(f"%{author}%")
        )

    if isbn is not None:
        query = query.where(
            BookModel.isbn == isbn
        )

    return session.scalars(query).all()


@with_session
def get_all_books(session):
    return session.scalars(
        select(BookModel)
    ).all()


@with_session
def add_user(session, name: str, user_type: str) -> bool:
    user = UserModel(
        name=name,
        user_type=user_type
    )

    session.add(user)

    return True


@with_session
def get_all_users(session):
    return session.scalars(
        select(UserModel)
    ).all()


@with_session
def remove_user(session, user_id: int) -> bool:
    user = session.get(UserModel, user_id)

    if user is None:
        return False

    active_borrowing = session.scalar(
        select(BorrowingModel).where(
            BorrowingModel.user_id == user_id,
            BorrowingModel.returned_at.is_(None)
        )
    )

    if active_borrowing is not None:
        return False

    session.delete(user)

    return True


@with_session
def borrow_book(session, user_id: int, book_id: int) -> str:
    user = session.get(UserModel, user_id)
    book = session.get(BookModel, book_id)

    if user is None:
        return "User not found"

    if book is None:
        return "Book not found"

    if not book.available:
        return "Book is not available"

    limits = {
        "student": (3, 14),
        "faculty": (10, 30),
        "guest": (1, 7)
    }

    user_type = user.user_type.lower()

    if user_type not in limits:
        return "Invalid user type"

    max_books, borrow_days = limits[user_type]

    active_borrowings = session.scalars(
        select(BorrowingModel).where(
            BorrowingModel.user_id == user_id,
            BorrowingModel.returned_at.is_(None)
        )
    ).all()

    if len(active_borrowings) >= max_books:
        return "Borrowing limit reached"

    today = date.today()

    borrowing = BorrowingModel(
        book_id=book_id,
        user_id=user_id,
        borrowed_at=today,
        due_date=today + timedelta(days=borrow_days)
    )

    book.available = False

    session.add(borrowing)

    return "Book borrowed successfully"


@with_session
def return_book(session, book_id: int) -> str:
    borrowing = session.scalar(
        select(BorrowingModel).where(
            BorrowingModel.book_id == book_id,
            BorrowingModel.returned_at.is_(None)
        )
    )

    if borrowing is None:
        return "Book is not currently borrowed"

    borrowing.returned_at = date.today()
    borrowing.book.available = True

    return "Book returned successfully"


@with_session
def get_overdue_books(session):
    today = date.today()

    return session.scalars(
        select(BorrowingModel).where(
            BorrowingModel.due_date < today,
            BorrowingModel.returned_at.is_(None)
        )
    ).all()

@with_session
def get_available_books(session):
    return session.scalars(
        select(BookModel).where(BookModel.available.is_(True))
    ).all()