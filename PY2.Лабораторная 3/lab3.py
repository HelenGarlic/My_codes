class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self.pages_new

    @pages.setter
    def pages(self, pages_new: int):
        if not isinstance(pages_new, int):
            raise TypeError
        if pages_new < 0:
            raise ValueError
        self.pages_new = pages_new

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Страниц {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self.duration_new

    @duration.setter
    def duration(self, duration_new: float) -> None:
        if not isinstance(duration_new, float):
            raise TypeError
        if duration_new < 0:
            raise ValueError
        self.duration_new = duration_new

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Длительность {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration}"


print(PaperBook("Стихи", "Пушкин", 500))
print(AudioBook("Стихи", "Пушкин", 1.20))

