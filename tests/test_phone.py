from src.phone import Phone
import pytest


@pytest.fixture
def phone():
    return Phone('Nokia', 50000, 10, 2)


def test_initial(phone):
    assert phone.name == 'Nokia'
    assert phone.price == 50000
    assert phone.quantity == 10
    assert phone.number_of_sim == 2
    assert repr(phone) == "Phone('Nokia', 50000, 10, 2)"
    assert str(phone) == 'Nokia'


def test_add(phone):
    phone1 = Phone('Samsung', 60000, 20, 1)
    assert phone + phone1 == 30
    assert phone + phone == 20


def test_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
