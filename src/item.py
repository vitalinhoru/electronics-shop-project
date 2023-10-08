import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        """
        Getter для name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Setter для name
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, filename):
        """
        Загружает данные из csv
        """
        Item.all.clear()
        current_dir = os.path.dirname(__file__)  # возвращает имя директории пути path
        root_dir = os.path.split(current_dir)[0]  # разбивает путь на кортеж (голова, хвост)
        filepath = os.path.join(root_dir, filename)  # соединяет пути
        if os.path.isfile(filepath):
            with open(filepath, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for i in reader:
                    items = cls(name=i.get('name'), price=i.get('price'), quantity=i.get('quantity'))

    @staticmethod
    def string_to_number(str_number):
        """
        Возвращает число из числа-строки
        """
        number = int(float(str_number.replace(',', '.')))
        return number
