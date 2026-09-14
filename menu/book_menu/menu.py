from menu.base import Menu, Option
from menu.book_menu.logic import (
    add_book_action,
    remove_book_action,
    search_by_title,
    search_by_author,
    search_by_isbn,
    show_books,
)

def create_book_menu():
    return Menu(
        "Book menu",
        [
            Option("Add book", None, add_book_action),
            Option("Remove book", None, remove_book_action),
            Option("Search by title", None, search_by_title),
            Option("Search by author", None, search_by_author),
            Option("Search by ISBN", None, search_by_isbn),
            Option("Show all books", None, show_books),
            Option("Borrow / return", None, lambda: "Borrow / return"),
            Option("Return to main menu", None, lambda: "Returned")
        ]
    )