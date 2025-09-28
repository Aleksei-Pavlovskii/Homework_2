from abc import ABC

from src.base_class import BaseClass


def test_base_class() -> None:
    assert issubclass(BaseClass, ABC)
    abstract_methods = BaseClass.__abstractmethods__
    assert "__init__" in abstract_methods
    assert "__str__" in abstract_methods


class NewClass(BaseClass):
    def __init__(self) -> None:
        self.data = "test"

    def __str__(self) -> str:
        return f"testing {self.data}"


obj = NewClass()
assert str(obj) == "testing test"
