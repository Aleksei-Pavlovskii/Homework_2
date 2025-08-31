class Category:
    """Класс для представления категорий товаров."""

    name: str
    description: str
    products: list
    count_category = 0
    count_products = 0

    def __init__(self, name: str, description: str, products: list | None = None):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.count_category += 1
        Category.count_products += len(products) if products else 0
