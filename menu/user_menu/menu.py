from menu.base import Menu, Option
from menu.user_menu.logic import (
    add_user_action,
    remove_user_action,
    show_users,
)


def create_user_menu():
    return Menu(
        "User menu",
        [
            Option("Add user", None, add_user_action),
            Option("Remove user", None, remove_user_action),
            Option("Show users", None, show_users),
            Option("Return to main menu", None, lambda: "Returned")
        ]
    )