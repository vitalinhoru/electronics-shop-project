from src.item import Item


class MixinKeyboard:
    layout = {'EN': 'RU', 'RU': 'EN'}

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def layout_lang(self):
        return self.__language

    def change_lang(self):
        self.__language = MixinKeyboard.layout.get(self.__language)


class Keyboard(MixinKeyboard, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.layout_lang()
