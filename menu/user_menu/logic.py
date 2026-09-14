from database.logic import (
    add_user, 
    get_all_users, 
    remove_user
)


def add_user_action():
    name = input("Name: ").strip()

    if not name:
        return "Name is required"

    print("0: Student")
    print("1: Faculty")
    print("2: Guest")

    try:
        user_type = int(input("Type: "))
    except ValueError:
        return "Invalid type"

    types = {
        0: "student",
        1: "faculty",
        2: "guest"
    }

    if user_type not in types:
        return "Invalid type"

    add_user(name, types[user_type])

    return "User added successfully"


def remove_user_action():
    try:
        user_id = int(input("User ID: "))
    except ValueError:
        return "Invalid user ID"

    if remove_user(user_id):
        return "User removed successfully"

    return "User does not exist or has borrowed books"


def show_users():
    users = get_all_users()

    if not users:
        return "No users found"

    return "\n".join(
        f"{user.id}: {user.name} | {user.user_type}"
        for user in users
    )