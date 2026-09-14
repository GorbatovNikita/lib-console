from menu.start_menu.menu import create_start_menu
from menu.book_menu.menu import create_book_menu
from menu.user_menu.menu import create_user_menu
from menu.borrow_menu.menu import create_borrow_menu


def build_menus():
    start_menu = create_start_menu()
    book_menu = create_book_menu()
    user_menu = create_user_menu()
    borrow_menu = create_borrow_menu()

    start_menu.get_option_list()[0].next_menu = book_menu
    start_menu.get_option_list()[1].next_menu = user_menu

    for option in book_menu.get_option_list()[:-1]:
        option.next_menu = book_menu

    book_menu.get_option_list()[-2].next_menu = borrow_menu
    book_menu.get_option_list()[-1].next_menu = start_menu

    for option in user_menu.get_option_list():
        option.next_menu = user_menu

    for option in borrow_menu.get_option_list():
        option.next_menu = borrow_menu

    borrow_menu.get_option_list()[-1].next_menu = start_menu
    user_menu.get_option_list()[-1].next_menu = start_menu

    return start_menu