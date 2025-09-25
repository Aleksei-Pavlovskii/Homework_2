from typing import Any, Iterator


class ProductsIterator:
    """Класс для итерирования по списку продуктов"""

    data: list

    def __init__(self, data: list):
        self.data = data
        self.index = 0

    def __iter__(self) -> Iterator:
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
