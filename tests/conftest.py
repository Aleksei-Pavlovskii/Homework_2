import pytest

from src.category_products import Category
from src.product import LawnGrass, Product, Smartphone


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


@pytest.fixture
def first_product() -> Product:
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет 200MP камера", 180000.0, 5)


@pytest.fixture
def second_product() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 21000.0, 7)


@pytest.fixture
def test_data() -> list:
    return ["product1", "product2", "product3"]


@pytest.fixture
def product_smartphone() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def product_grass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def category_none_list_product() -> Category:
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником",
        [],
    )
