from unittest.mock import Mock, mock_open, patch

from src.utils import create_objects_from_json, read_json


@patch("os.path.exists")
def test_read_json(mock_os: Mock) -> None:
    mock_os.return_value = True
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert read_json("a") == {"1": "2"}


def test_create_objects_from_json(dict_category: list[dict]) -> None:
    result = create_objects_from_json(dict_category)
    category = result[0]
    assert category.name == "Телевизоры"
    assert (
        category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    product = category.products[0]
    assert product.name == '55" QLED 4K'
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7
