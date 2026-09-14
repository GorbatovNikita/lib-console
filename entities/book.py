class Book:
    def __init__(
        self,
        title: str,
        author: str,
        isbn: str,
        available: bool = True
    ):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = available

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_isbn(self) -> str:
        return self.__isbn

    def is_available(self) -> bool:
        return self.__available

    def set_available(self, available: bool):
        self.__available = available

    def __str__(self):
        status = "Available" if self.__available else "Borrowed"

        return (
            f"{self.__title} | "
            f"{self.__author} | "
            f"{self.__isbn} | "
            f"{status}"
        )