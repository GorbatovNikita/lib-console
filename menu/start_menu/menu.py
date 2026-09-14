from menu.base import Menu, Option


def create_start_menu():
    return Menu(
        "Main menu",
        [
            Option("Book management", None, lambda: "Book management"),
            Option( "User management", None, lambda: "User management")
        ]
    )