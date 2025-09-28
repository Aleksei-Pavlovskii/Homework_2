from src.order import Order
from src.product import Product


def test_order(first_product: Product) -> None:
    order = Order(first_product, 5)
    assert order.product == first_product
    assert order.quantity == 5
    assert isinstance(order, Order)


def test_order_total_price(first_product: Product) -> None:
    order = Order(first_product, 2)
    assert order.total_price == 360000.0


def test_str_order(first_product: Product) -> None:
    order = Order(first_product, 2)
    assert str(order) == "Наименование: Samsung Galaxy C23 Ultra, количество: 2, общая стоимость: " "360000.0"
