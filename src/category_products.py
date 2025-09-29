from typing import Any

from src.base_class import BaseClass
from src.product import Product


class Category(BaseClass):
    """Класс для представления категорий товаров."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        list_quantity = []
        for product in self.__products:
            list_quantity.append(product.quantity)
        return f"{self.name}, количество продуктов: {sum(list_quantity)} шт."

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, product: Any) -> None:
        """Метод, который добавляет новый товар в список товаров"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Возникла ошибка TypeError при добавлении не продукта")

    @property
    def products_in_list(self) -> list:
        return self.__products

    def middle_price(self) -> Any:
        """Метод, который подсчитывает средний ценник всех товаров"""
        list_price = []
        try:
            for product in self.__products:
                list_price.append(product.price)
            return round(sum(list_price) / len(list_price), 2)
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
            return 0
