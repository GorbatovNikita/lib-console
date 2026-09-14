from database.database import initialize_database
from menu.menu_builder import build_menus


initialize_database()

type_menu = build_menus()

command = 0
current_menu = type_menu

while command != -1:
    print(current_menu.get_title())

    current_option_list = current_menu.get_option_list()

    for index, option in enumerate(current_option_list):
        print(f"{index}: {option.get_title()}")

    try:
        command = int(input())
    except ValueError:
        print("Please enter a number.")
        print("-" * 10)
        continue

    if command == -1:
        break

    if command < 0 or command >= len(current_option_list):
        print("Invalid option.")
        print("-" * 10)
        continue

    current_option = current_option_list[command]

    print(current_option.execute())

    current_menu = (
        current_option.get_next_menu()
        if current_option.get_next_menu() is not None
        else type_menu
    )

    print("-" * 10)