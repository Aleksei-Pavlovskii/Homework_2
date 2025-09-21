import pytest

from src.category_products import Category
from src.product import Product


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def product() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def dict_category() -> list[dict]:
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
                           "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]


@pytest.fixture
def new_product() -> dict:
    return {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}


@pytest.fixture
def list_products() -> list:
    return [
        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет 200MP камера", 180000.0, 5),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 21000.0, 7),
    ]
