import pytest

from src.products_iterator import ProductsIterator


def test_product_iterator(test_data: list) -> None:
    iterator = ProductsIterator(test_data)
    result = list(iterator)
    assert result == test_data


def test_product_iterator_raises() -> None:
    iterator = ProductsIterator(["product1"])
    next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)
