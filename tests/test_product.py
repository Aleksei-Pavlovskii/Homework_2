from unittest.mock import patch

import pytest

from src.product import LawnGrass, Product, Smartphone


def test_product_init(product: Product) -> None:
    """Тест инициализации класса Product"""

    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_new_product(new_product: dict) -> None:
    """Тест добавления нового продукта"""

    result = Product.new_product(new_product)
    assert result.name == "Xiaomi Redmi Note 11"
    assert result.description == "1024GB, Синий"
    assert result.price == 31000.0
    assert result.quantity == 14


def test_new_product_add(new_product: dict, list_products: list) -> None:
    """Тест обновления продукта"""

    result = Product.new_product(new_product, list_products)
    assert result is list_products[1]
    assert result.quantity == 21
    assert result.price == 31000.0


def test_price_setter(product: Product) -> None:
    """Тест на изменение цены"""

    product.price = 0
    assert product.price == 31000.0
    with patch("builtins.input", return_value="y"):
        product.price = 21000.0
    assert product.price == 21000.0


def test_str_product(product: Product) -> None:
    """Тест вывода строки"""
    assert str(product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_add_product(first_product: Product, second_product: Product) -> None:
    """Тест сложения двух продуктов"""
    assert first_product + second_product == 1047000.0


def test_add_product_raise(product_smartphone: Smartphone, product_grass: LawnGrass) -> None:
    """Тест для проверки сложения разных классов продуктов"""
    with pytest.raises(TypeError):
        product_smartphone + product_grass


def test_smartphone_init(product_smartphone: Smartphone) -> None:
    """Тест инициализации класса Smartphone"""
    assert product_smartphone.efficiency == 95.5
    assert product_smartphone.model == "S23 Ultra"
    assert product_smartphone.memory == 256
    assert product_smartphone.color == "Серый"


def test_lawn_grass_init(product_grass: LawnGrass) -> None:
    """Тест инициализации класса LawnGrass"""
    assert product_grass.country == "Россия"
    assert product_grass.germination_period == "7 дней"
    assert product_grass.color == "Зеленый"


def test_product_init_raises() -> None:
    with pytest.raises(ValueError):
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)
