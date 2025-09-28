from src.base_class import BaseClass
from src.product import Product


class Order(BaseClass):
    """Класс для представления заказов"""

    def __init__(self, product: Product, quantity: int) -> None:
        """Метод, который инициализирует экземпляры класса."""
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"Наименование: {self.product.name}, количество: {self.quantity}, общая стоимость: {self.total_price}"
