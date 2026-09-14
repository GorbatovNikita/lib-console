from entities.user import User


class Faculty(User):
    def get_borrow_limit(self) -> int:
        return 10

    def get_borrow_days(self) -> int:
        return 30