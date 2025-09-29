from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный класс для класса Продуктов"""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> Any:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> Any:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        pass


class MixinInfo:
    """Класс миксин для вывода информации о товаре"""

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinInfo, BaseProduct):
    """Класс для представления категорий товаров."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод, который инициализирует экземпляры класса."""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        if self.quantity == 0:
            print("Товар с нулевым количеством не может быть добавлен")
            raise ValueError

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Возникла ошибка TypeError при попытке сложения")

    @classmethod
    def new_product(cls, product: dict, product_list: Any | None = None) -> Any:
        """Клас-метод который создает новый продукт или обновляет существующий"""
        if product_list is None:
            product_list = []

        for existing_product in product_list:
            if existing_product.name == product["name"]:
                existing_product.quantity += product["quantity"]

                if product["price"] > existing_product.price:
                    existing_product.price = product["price"]

                return existing_product

        return cls(**product)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            print(
                'Новая цена ниже старой, если хотите изменить введите "y", '
                "чтобы отменить изменение введите любой символ"
            )
            user_input = input()
            if user_input.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price


class Smartphone(Product):
    """Класс для представления категории смартфоны."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления категории трава газонная."""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
