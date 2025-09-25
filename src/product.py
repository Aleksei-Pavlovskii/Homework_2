from typing import Any


class Product:
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

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> Any:
        return self.price * self.quantity + other.price * other.quantity

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
    def price(self, new_price: int) -> None:
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
