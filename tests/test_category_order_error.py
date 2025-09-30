from src.category_order_error import CategoryOrderError, NoneQuantityError


def test_category_order_error_default_message() -> None:
    """Тест CategoryOrderError с сообщением по умолчанию"""
    error = CategoryOrderError()
    assert str(error) == "Неизвестная ошибка"
    assert error.message == "Неизвестная ошибка"


def test_none_quantity_error_default_message() -> None:
    """Тест NoneQuantityError с сообщением по умолчанию"""
    error = NoneQuantityError()
    assert str(error) == "Количество равно 0"
    assert error.message == "Количество равно 0"
