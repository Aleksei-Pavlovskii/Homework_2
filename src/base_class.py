from abc import ABC, abstractmethod


class BaseClass(ABC):
    """Абстрактный класс для классов Категории и Заказы"""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
