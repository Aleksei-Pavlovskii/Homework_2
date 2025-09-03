import json
import os
from typing import Any

from src.category_products import Category
from src.product import Product


def read_json(path: str) -> Any:

    """Функция, которая читает JSON файл"""
    full_path = os.path.abspath((path))
    with open(full_path, encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list[dict]) -> list:
    """Функция, которая создает объект из JSON"""

    categores = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categores.append(Category(**category))
    return categores
