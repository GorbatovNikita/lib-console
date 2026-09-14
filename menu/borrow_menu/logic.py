from database.logic import (
    borrow_book,
    return_book,
    get_overdue_books,
    get_available_books,
)


def borrow_book_action():
    try:
        user_id = int(input("User ID: "))
        book_id = int(input("Book ID: "))
    except ValueError:
        return "IDs must be numbers"

    return borrow_book(user_id, book_id)


def show_available_books():
    books = get_available_books()

    if not books:
        return "No available books"

    return "\n".join(
        f"{book.id}: {book.title} | "
        f"{book.author} | "
        f"{book.isbn}"
        for book in books
    )


def return_book_action():
    try:
        book_id = int(input("Book ID: "))
    except ValueError:
        return "Book ID must be a number"

    return return_book(book_id)


def overdue_books_action():
    borrowings = get_overdue_books()

    if not borrowings:
        return "No overdue books"

    return "\n".join(
        f"Book: {borrowing.book.title} | "
        f"User: {borrowing.user.name} | "
        f"Due: {borrowing.due_date}"
        for borrowing in borrowings
    )