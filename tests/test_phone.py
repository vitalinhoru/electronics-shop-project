from src.item import Item
from src.phone import Phone
import pytest


def test_phone():
    phone = Phone('Nokia', 50000, 10, 2)
    assert repr(phone) == "Phone('Nokia', 50000, 10, 2)"
    assert str(phone) == 'Nokia'
    assert phone.number_of_sim == 2
    item = Item("Samsung", 70000, 20)
    assert item + phone == 30
    assert phone + phone == 20
    phone1 = Phone('Nokia', 50000, 10, 0)
    assert phone1.number_of_sim == 0

def test_number_of_sim():
    phone = Phone('Nokia', 50000, 10, 2)
    with pytest.raises(ValueError):
        phone.number_of_sim = 0