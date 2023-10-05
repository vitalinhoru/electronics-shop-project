"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item = Item(name='milk', price=80, quantity=10)
    assert item.name == 'milk'
    assert item.price == 80
    assert item.quantity == 10


def test_calculate_total_price():
    item = Item(name='milk', price=80, quantity=10)
    assert item.calculate_total_price() == 800


def test_apply_discount():
    item = Item(name='milk', price=80, quantity=10)
    assert item.price == 80
    Item.pay_rate = 1.5
    assert item.apply_discount() is None
    assert item.price == 120
