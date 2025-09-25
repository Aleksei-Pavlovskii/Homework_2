from unittest.mock import patch

from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_new_product(new_product: dict) -> None:
    result = Product.new_product(new_product)
    assert result.name == "Xiaomi Redmi Note 11"
    assert result.description == "1024GB, Синий"
    assert result.price == 31000.0
    assert result.quantity == 14


def test_new_product_add(new_product: dict, list_products: list) -> None:
    result = Product.new_product(new_product, list_products)
    assert result is list_products[1]
    assert result.quantity == 21
    assert result.price == 31000.0


def test_price_setter(product: Product) -> None:
    product.price = 0
    assert product.price == 31000.0
    with patch("builtins.input", return_value="y"):
        product.price = 21000.0
    assert product.price == 21000.0


def test_str_product(product: Product) -> None:
    assert str(product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_add_product(first_product: Product, second_product: Product) -> None:
    assert first_product + second_product == 1047000.0
