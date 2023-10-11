"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


# def test_item():
#     item = Item(name = 'milk', price = 80, quantity = 10)
#     assert item.name == 'milk'
#     assert item.price == 80
#     assert item.quantity == 10
#
#
# def test_calculate_total_price():
#     item = Item(name = 'milk', price = 80, quantity = 10)
#     assert item.calculate_total_price() == 800
#
#
# def test_apply_discount():
#     item = Item(name = 'milk', price = 80, quantity = 10)
#     assert item.price == 80
#     Item.pay_rate = 1.5
#     assert item.apply_discount() is None
#     assert item.price == 120

@pytest.fixture
def item() -> Item:
    return Item("Смартфон", 1000, 2)


def test_item_initialized(item) -> None:
    assert item.name == "Смартфон"
    assert item.price == 1000
    assert item.quantity == 2


def test_calculate_total_price(item) -> None:
    assert item.calculate_total_price() == 2000


def test_apply_discount(item) -> None:
    item.pay_rate = 0.8


def test_name(item):
    item.name = '1234567890а это уже не пишется'
    assert item.name == '1234567890'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_convert_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5,0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr(item):
    assert repr(item) == "Item('Смартфон', 1000, 2)"

def test_str(item):
    assert str(item) == 'Смартфон'