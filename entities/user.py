from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    @abstractmethod
    def get_borrow_limit(self) -> int:
        pass

    @abstractmethod
    def get_borrow_days(self) -> int:
        pass