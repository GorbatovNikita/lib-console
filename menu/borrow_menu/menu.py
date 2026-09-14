from menu.base import Menu, Option
from menu.borrow_menu.logic import (
    show_available_books,
    borrow_book_action,
    return_book_action,
    overdue_books_action
)


def create_borrow_menu():
    return Menu(
        "Borrow menu",
        [
            Option("Show available books", None, show_available_books),
            Option("Borrow book", None, borrow_book_action),
            Option("Return book", None, return_book_action),
            Option("View overdue books", None, overdue_books_action),
            Option("Return to main menu", None, lambda : "Success")
        ]
    )