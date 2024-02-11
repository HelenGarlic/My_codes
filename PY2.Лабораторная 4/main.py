class Films:
    """
    Документация на базовый класс.
    Класс описывает модель фильмы.
    Атрибуты name, year, duration изменяться не могут.
    """
    def __init__(self, id_: int, name: str, year: int, genre: str, actors: list[str], duration: int, rate: float):
        self.id_ = id_
        self._name = name
        self._year = year
        self.genre = genre
        self.actors = actors
        self._duration = duration
        self.rate = rate

    def __str__(self) -> str:
        return f"Id фильма {self.id_}. Фильм {self._name}. Дата выхода {self._year}. Жанр {self.genre}." \
               f" Актеры и роли {self.actors}. Длительность {self._duration} мин. Средняя оценка {self.rate}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id_}, name={self._name!r}, year={self._year}," \
               f" genre={self.genre!r}, actors={self.actors!r}, duration={self._duration}, rate={self.rate})"

    def what_century(self) -> str:
        "Функция, которая указывает в каком веке выпущен фильм"
        return f"'{self._name}' выпущен в {(self._year - 1 )// 100 + 1} веке."

    def give_a_rate(self, name, users_rate, counts) -> str:
        """
        Функция которая запрашивает у пользователя оценку и выставляет среднюю, суммируя оценки
        и деля на количество оценок на фильм
        Пример:
        >> film_1 = Films(name, users_rate)
        >> film_1.give_a_rate()
        Вывод:
        Спасибо за оценку. Теперь у фильма рейтинг {new_rate}
        """
        ...


class Cartoons(Films):
    """
    Документация на дочерний класс.
    Класс описывает модель мультфильмы.
    Атрибуты name, year, duration изменяться не могут.
    """
    def __init__(self, id_: int, name: str, year: int, voice_actors: list[str], duration: int, graphics: str, rate: float):
        super().__init__(id_, name, year, "genre", "actors", duration, rate)
        self.voice_actors = voice_actors
        self.graphics = graphics

    def __str__(self) -> str:
        return f"Id мультфильма {self.id_}. Фильм {self._name}. Дата выхода {self._year}. " \
               f"Актеры озвучки и роли {self.voice_actors}.Длительность {self._duration} мин. Графика {self.graphics!r}. Средняя оценка {self.rate}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id_}, name={self._name!r}, year={self._year}," \
               f" voice_actors={self.voice_actors!r}, duration={self._duration}, graphics={self.graphics!r}, rate={self.rate})"

    def what_century(self) -> str:
        """
        Аналогичный метод из класса Фильмы.
        """
        return super().what_century()

if __name__ == "__main__":
    first_film = Films(112, "Аватар", 2009, "фантастика", ["Сэм Уортингтон", "Зои Салдана", "Сигурни Уивер", "Стивен Лэнг"], 162, 0.0)
    first_cartoon = Cartoons(113, "Шрек", 2001, ["Майк Майерс", "Эдди Мерфи", "Кэмерон Диас"], 90, "2D", 5.0)
    print(first_film)
    print(Films.what_century(first_film))
    print(first_cartoon)
    print(Cartoons.what_century(first_cartoon))
    pass
