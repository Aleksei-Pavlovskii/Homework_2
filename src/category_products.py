from typing import Any


class Category:
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

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def add_product(self, product: Any) -> None:
        """Метод, который добавляет новый товар в список товаров"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self) -> list:
        return self.__products
