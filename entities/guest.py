from entities.user import User


class Guest(User):
    def get_borrow_limit(self) -> int:
        return 1

    def get_borrow_days(self) -> int:
        return 7