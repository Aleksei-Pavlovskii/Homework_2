import pytest

from src.category_products import Category
from src.product import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description == "Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни"
    )
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_products_property(first_category: Category) -> None:
    assert first_category.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_add_product(first_category: Category, product: Product) -> None:
    assert len(first_category.products_in_list) == 2
    first_category.add_product(product)
    assert len(first_category.products_in_list) == 3


def test_add_product_not_product(first_category: Category) -> None:
    with pytest.raises(TypeError):
        first_category.add_product("product")


def test_str_category(first_category: Product) -> None:
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_middle_price(first_category: Category) -> None:
    assert first_category.middle_price() == 195000.0


def test_middle_price_none_list_product(category_none_list_product: Category) -> None:
    assert category_none_list_product.middle_price() == 0
