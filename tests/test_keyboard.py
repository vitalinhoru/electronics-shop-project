from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard():
    return Keyboard('Logitech', 5000, 2)


def test_initial(keyboard):
    assert keyboard.name == 'Logitech'
    assert keyboard.price == 5000
    assert keyboard.quantity == 2


def test_layout_lang(keyboard):
    assert keyboard.language == 'EN'

    keyboard.change_lang()
    assert keyboard.language == "RU"

    keyboard.change_lang()
    assert keyboard.language == "EN"


def test_wrong_lang(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'
