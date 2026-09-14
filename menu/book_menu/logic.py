from database.logic import (
    add_book,
    remove_book,
    search_books,
    get_all_books
)


def add_book_action():
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()

    if not title or not author or not isbn:
        return "All fields are required"

    if add_book(title, author, isbn):
        return "Book added successfully"

    return "Book with this ISBN already exists"


def remove_book_action():
    isbn = input("ISBN: ").strip()

    if remove_book(isbn):
        return "Book removed successfully"

    return "Book does not exist or is currently borrowed"


def search_by_title():
    title = input("Title: ").strip()

    books = search_books(title=title)

    if not books:
        return "No books found"

    return "\n".join(
        f"{book.id}: {book.title} | "
        f"{book.author} | "
        f"{book.isbn} | "
        f"{'Available' if book.available else 'Borrowed'}"
        for book in books
    )


def search_by_author():
    author = input("Author: ").strip()

    books = search_books(author=author)

    if not books:
        return "No books found"

    return "\n".join(
        f"{book.id}: {book.title} | "
        f"{book.author} | "
        f"{book.isbn} | "
        f"{'Available' if book.available else 'Borrowed'}"
        for book in books
    )


def search_by_isbn():
    isbn = input("ISBN: ").strip()

    books = search_books(isbn=isbn)

    if not books:
        return "No books found"

    return "\n".join(
        f"{book.id}: {book.title} | "
        f"{book.author} | "
        f"{book.isbn} | "
        f"{'Available' if book.available else 'Borrowed'}"
        for book in books
    )


def show_books():
    books = get_all_books()

    if not books:
        return "Library is empty"

    return "\n".join(
        f"{book.id}: {book.title} | "
        f"{book.author} | "
        f"{book.isbn} | "
        f"{'Available' if book.available else 'Borrowed'}"
        for book in books
    )
