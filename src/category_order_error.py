class CategoryOrderError(Exception):
    """Клас для ошибок"""

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        self.message = args[0] if args else "Неизвестная ошибка"

    def __str__(self) -> tuple | str:
        return self.message


class NoneQuantityError(CategoryOrderError):
    """Класс ошибки при добавление товара с количество равное нулю"""

    def __init__(self, *args: tuple) -> None:
        self.message = args[0] if args else "Количество равно 0"
