from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_num):
        if new_num > 0:
            self.__number_of_sim = int(new_num)
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
