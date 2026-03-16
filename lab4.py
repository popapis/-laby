class Book:
    """
    Базовый класс, представляющий печатную или электронную книгу.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализирует объект книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц.
        """
        self.title = title
        self.author = author

        # Инкапсулируем количество страниц, чтобы предотвратить
        # установку отрицательного или нулевого значения напрямую извне.
        self._pages = pages

    def get_info(self) -> str:
        """
        Возвращает базовую информацию о книге.
        Этот метод будет унаследован дочерним классом без изменений.
        """
        return f"Книга: '{self.title}', Автор: {self.author}"

    def read(self) -> str:
        """
        Имитирует процесс чтения книги.
        """
        return f"Вы читаете книгу '{self.title}' глазами. В ней {self._pages} страниц."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта, удобное для пользователя.
        """
        return f"'{self.title}' ({self.author})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки и разработчиков.
        """
        return f"{self.__class__.__name__}(title='{self.title}', author='{self.author}', pages={self._pages})"


class AudioBook(Book):
    """
    Дочерний класс, представляющий аудиокнигу.
    Наследуется от класса Book.
    """

    def __init__(self, title: str, author: str, duration_minutes: int, narrator: str):
        """
        Расширяет конструктор базового класса.
        Аудиокниги не измеряются в страницах (передаем 0), но у них есть длительность и чтец.

        :param title: Название аудиокниги.
        :param author: Автор книги.
        :param duration_minutes: Длительность аудиокниги в минутах.
        :param narrator: Имя чтеца (диктора).
        """
        # Вызов конструктора базового класса. Страниц нет, поэтому передаем 0.
        super().__init__(title, author, pages=0)

        self.duration_minutes = duration_minutes
        self.narrator = narrator

    def read(self) -> str:
        """
        Перегруженный метод read.

        Причина перегрузки: Аудиокнигу не читают глазами (по страницам), 
        её слушают (по времени). Поэтому логика потребления контента 
        меняется, и метод должен отражать этот факт.
        """
        return f"Вы слушаете аудиокнигу '{self.title}' (чтец: {self.narrator}). Длительность: {self.duration_minutes} мин."

    def __str__(self) -> str:
        """
        Перегруженный магический метод __str__ для добавления информации о формате.
        """
        return f"[Аудиокнига] '{self.title}' ({self.author}) - читает {self.narrator}"

    def __repr__(self) -> str:
        """
        Перегруженный магический метод __repr__ с учетом новых атрибутов.
        """
        return f"{self.__class__.__name__}(title='{self.title}', author='{self.author}', duration_minutes={self.duration_minutes}, narrator='{self.narrator}')"


if __name__ == "__main__":
    # Создаем экземпляр базового класса
    my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 480)

    # Создаем экземпляр дочернего класса
    my_audiobook = AudioBook("Дюна", "Фрэнк Герберт", 1260, "Сергей Чонишвили")

    print("--- Проверка базового класса Book ---")
    print(f"__str__:  {my_book}")
    print(f"__repr__: {repr(my_book)}")
    print(f"Метод get_info: {my_book.get_info()}")
    print(f"Метод read:     {my_book.read()}")
    print("\n")

    print("--- Проверка дочернего класса AudioBook ---")
    print(f"__str__:  {my_audiobook}")
    print(f"__repr__: {repr(my_audiobook)}")

    # Демонстрация наследования метода
    print(f"Унаследованный метод get_info: {my_audiobook.get_info()}")

    # Демонстрация перегрузки метода
    print(f"Перегруженный метод read:      {my_audiobook.read()}")