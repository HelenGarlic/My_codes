import doctest


class ArtPiece:
    def __init__(self, artist: str, name_of_a_piece: str, year: int):
        """
        Создание и подготовка к работе объекта "Произведение искусства"

        :param artist: Художник
        :param name_of_a_piece: Произведение искусства
        :param year: Год создания произведения

        Примеры:
        >>> art_piece_1 = ArtPiece("Винсент ван Гог", "Подсолнухи", 1888)  # инициализация экземпляра класса
        """
        if not isinstance(artist, str):
            raise TypeError("Художник должен быть типом str")
        self.artist = artist

        if not isinstance(name_of_a_piece, str):
            raise TypeError("Произведение искусства должно быть типом str")
        self.name_of_a_piece = name_of_a_piece

        if not isinstance(year, int):
            raise TypeError("Год создания произведения должен быть типом int") #Если тип года не является int, то вызываем ошибку
        if not year > 0:
            raise ValueError("Год создания должен быть больше 0") #Если год является отрицателным числом, то вызываем ошибку
        self.year = year

    def is_artist_unknown(self) -> bool:
        """
        Метод который проверяет указан ли автор у работы.

        Примеры:
        >>> art_piece_2 = ArtPiece("Неизвестный художник", "Вид Дерби", 1725)
        >>> art_piece_2.is_artist_unknown()
        """
        ...

    def how_old_is_art_piece(self, current_year: int) -> int:
        """
        Метод который вычисляет сколько лет произведению искусства.
        :param current_year: Текущий год

        Примеры:
        >>> art_piece_1 = ArtPiece("Винсент ван Гог", "Подсолнухи", 1888)
        >>> art_piece_1.how_old_is_art_piece(2024)
        """
        if not isinstance(current_year, int):
            raise TypeError("Текущий год должен быть типа int") #Если тип текущего года не является int, то вызываем ошибку
        if current_year <= 0:
            raise ValueError("Текущий год должен быть больше 0") #Если текущий год является отрицателным числом, то вызываем ошибку
        self.current_year = current_year
        ...


class Person:
    def __init__(self, name: str, year_of_birth: int, gender: str):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: Имя и фамилия человека
        :param year_of_birth: Год рождения человека
        :param gender: Пол человека

        Примеры:
        >>> person_1 = Person("Александра Трусова", 2004, "ж")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типом str") #вызов ошибки
        self.name = name

        if not isinstance(year_of_birth, int):
            raise TypeError("Год рождения должен быть типом int") #вызов ошибки
        if year_of_birth <= 0:
            raise ValueError("Год рождения должен быть больше 0") #вызов ошибки
        self.year_of_birth = year_of_birth

        if not isinstance(gender, str):
            raise TypeError("Пол должен быть типом str") #вызов ошибки
        self.gender = gender

    def is_person_female(self) -> bool:
        """
        Функция которая проверяет женского ли пола человек.

        :return: Женского ли пола человек?

        Примеры:
        >>> person_1 = Person("Александра Трусова", 2004, "ж")
        >>> person_1.is_person_female()
        """
        ...

    def how_old_is_a_person(self, current_year: int) -> int:
        """
        Метод который выдает возраст человека
        :param current_year: Текущий год

        Примеры:
        >>> person_1 = Person("Александра Трусова", 2004, "ж") # инициализация экземпляра класса
        >>> person_1.how_old_is_a_person(2024)
        """
        if not isinstance(current_year, int):
            raise TypeError("Текущий год должен быть типа int") #Если тип текущего года не является int, то вызываем ошибку
        if current_year <= 0:
            raise ValueError("Текущий год должен быть положительным числом") #Если текущий год является отрицателным числом, то вызываем ошибку
        self.current_year = current_year
        ...


class Student:
    def __init__(self, name: str, grade: int, year_of_birth: int, gender: str, courses: dict):
        """
        Создание и подготовка к работе объекта "Ученик"

        :param name: Имя и фамилия ученика
        :param grade: Класс
        :param courses: Изучаемые предметы

        Примеры:
        >>> student_1 = Student("Мария Квадратова", 8, 2004, "ж", {"Математика" : 4, "ИЗО" : 5, "Физкультура" : 3})  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя и фамилия ученика должны быть типом str") #вызов ошибки
        self.name = name

        if not isinstance(grade, int):
            raise TypeError("Класс должен быть типа int") #вызов ошибки
        if not 0 > grade > 12:
            raise ValueError("Класс должен быть больше 0, но меньше 12") #вызов ошибки
        self.grade = grade

        if not isinstance(year_of_birth, int):
            raise TypeError("Год рождения должен быть типом int") #вызов ошибки
        if year_of_birth <= 0:
            raise ValueError("Год рождения должен быть больше 0") #вызов ошибки
        self.year_of_birth = year_of_birth

        if not isinstance(gender, str):
            raise TypeError("Пол должен быть типом str") #вызов ошибки
        self.gender = gender

        self.courses = courses
        ...

    def is_red_diploma(self, name: str, grade: int, courses: dict) -> bool:
        """
        Метод который проверяет получит ли ученик красный аттеста.

        Примеры:
        >>> student_2 = Student("Михаил Колесов", 10, {"Математика" : 4, "Русский язык" : 5, "Физкультура" : 5})
        >>> person_1.is_red_diploma()
        """
        ...

    def voenkomat(self, name: str, year_of_birth: int, gender: str) -> bool:
        """
        Метод который проверяет нужно ли ученику поставиться на учет в военкомате.

        Примеры:
        >>> student_1 = Student("Мария Квадратова", 8, 2004, "ж")
        >>> student_2 = Student("Михаил Колесов", 10, 2003, "м")
        >>> student_1.voenkomat()
        >>> student_2.voenkomat()
        """
        ...



if __name__ == "__main__":
    doctest.testmod()

