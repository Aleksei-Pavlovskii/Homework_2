from src.category_products import Category


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 2

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_products == 3
    assert second_category.count_products == 3
