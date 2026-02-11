# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Bicycle:
    def __init__(self, brand: str, wheel_size: float, gears: int):
        """
        Создание и подготовка к работе объекта "Велосипед"

        :param brand: Бренд велосипеда
        :param wheel_size: Размер колес в дюймах
        :param gears: Количество передач

        Примеры:
        >>> bike = Bicycle("Giant", 26.0, 21)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть типа str")
        if not brand.strip():
            raise ValueError("Бренд не может быть пустой строкой")
        self.brand = brand

        if not isinstance(wheel_size, (int, float)):
            raise TypeError("Размер колес должен быть типа int или float")
        if wheel_size <= 0:
            raise ValueError("Размер колес должен быть положительным")
        self.wheel_size = wheel_size

        if not isinstance(gears, int):
            raise TypeError("Количество передач должно быть типа int")
        if gears < 1:
            raise ValueError("Количество передач должно быть хотя бы 1")
        self.gears = gears

    def ride(self, distance: float) -> None:
        """
        Езда на велосипеде на заданное расстояние.

        :param distance: Расстояние в километрах
        :raise ValueError: Если расстояние отрицательное

        Примеры:
        >>> bike = Bicycle("Giant", 26.0, 21)
        >>> bike.ride(10.0)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        ...

    def change_gear(self, new_gear: int) -> None:
        """
        Переключение передачи.

        :param new_gear: Номер новой передачи
        :raise ValueError: Если номер передачи вне диапазона

        Примеры:
        >>> bike = Bicycle("Giant", 26.0, 21)
        >>> bike.change_gear(5)
        """
        if not isinstance(new_gear, int):
            raise TypeError("Номер передачи должен быть типа int")
        if new_gear < 1 or new_gear > self.gears:
            raise ValueError("Номер передачи должен быть в диапазоне от 1 до количества передач")
        ...

    def is_mountain_bike(self) -> bool:
        """
        Проверка, является ли велосипед горным (по размеру колес).

        :return: True если горный, иначе False

        Примеры:
        >>> bike = Bicycle("Giant", 26.0, 21)
        >>> bike.is_mountain_bike()
        """
        ...

class Movie:
    def __init__(self, title: str, director: str, duration: int):
        """
        Создание и подготовка к работе объекта "Фильм"

        :param title: Название фильма
        :param director: Режиссер
        :param duration: Продолжительность в минутах

        Примеры:
        >>> movie = Movie("Inception", "Christopher Nolan", 148)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть типа str")
        if not title.strip():
            raise ValueError("Название не может быть пустой строкой")
        self.title = title

        if not isinstance(director, str):
            raise TypeError("Режиссер должен быть типа str")
        if not director.strip():
            raise ValueError("Режиссер не может быть пустой строкой")
        self.director = director

        if not isinstance(duration, int):
            raise TypeError("Продолжительность должна быть типа int")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self.duration = duration

    def play(self) -> None:
        """
        Воспроизведение фильма.

        Примеры:
        >>> movie = Movie("Inception", "Christopher Nolan", 148)
        >>> movie.play()
        """
        ...

    def get_duration_in_hours(self) -> float:
        """
        Получить продолжительность в часах.

        :return: Продолжительность в часах

        Примеры:
        >>> movie = Movie("Inception", "Christopher Nolan", 148)
        >>> movie.get_duration_in_hours()
        """
        ...

    def add_subtitles(self, language: str) -> None:
        """
        Добавление субтитров на указанном языке.

        :param language: Язык субтитров

        Примеры:
        >>> movie = Movie("Inception", "Christopher Nolan", 148)
        >>> movie.add_subtitles("Russian")
        """
        if not isinstance(language, str):
            raise TypeError("Язык должен быть типа str")
        if not language.strip():
            raise ValueError("Язык не может быть пустой строкой")
        ...

class Library:
    def __init__(self, name: str, books_count: int, location: str):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param name: Название библиотеки
        :param books_count: Количество книг
        :param location: Местоположение

        Примеры:
        >>> library = Library("Central Library", 50000, "City Center")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if not name.strip():
            raise ValueError("Название не может быть пустой строкой")
        self.name = name

        if not isinstance(books_count, int):
            raise TypeError("Количество книг должно быть типа int")
        if books_count < 0:
            raise ValueError("Количество книг не может быть отрицательным")
        self.books_count = books_count

        if not isinstance(location, str):
            raise TypeError("Местоположение должно быть типа str")
        if not location.strip():
            raise ValueError("Местоположение не может быть пустой строкой")
        self.location = location

    def add_book(self, book_title: str) -> None:
        """
        Добавление книги в библиотеку.

        :param book_title: Название книги

        Примеры:
        >>> library = Library("Central Library", 50000, "City Center")
        >>> library.add_book("New Book")
        """
        if not isinstance(book_title, str):
            raise TypeError("Название книги должно быть типа str")
        if not book_title.strip():
            raise ValueError("Название книги не может быть пустой строкой")
        ...

    def remove_book(self, book_title: str) -> None:
        """
        Удаление книги из библиотеки.

        :param book_title: Название книги
        :raise ValueError: Если книга не найдена

        Примеры:
        >>> library = Library("Central Library", 50000, "City Center")
        >>> library.remove_book("Old Book")
        """
        if not isinstance(book_title, str):
            raise TypeError("Название книги должно быть типа str")
        if not book_title.strip():
            raise ValueError("Название книги не может быть пустой строкой")
        ...

    def is_large(self) -> bool:
        """
        Проверка, является ли библиотека большой (более 10000 книг).

        :return: True если большая, иначе False

        Примеры:
        >>> library = Library("Central Library", 50000, "City Center")
        >>> library.is_large()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации