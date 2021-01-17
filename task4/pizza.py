from abc import ABC, abstractmethod
from handout import Handout


class Pizza(ABC, Handout):
    name_dict = {1: "Пицца 'Пеперони'", 2: "Пицца 'Барбекю'", 3: "Пицца 'Дары Моря'"}
    dough_dict = {0: "стандартное", 1: "тонкое", 2: "толстое"}
    sauce_dict = {0: "нет", 1: "томатный", 2: "сырный", 3: "чесночный"}
    sauce_price_dict = {"нет": 0, "томатный": 25, "сырный": 35, "чесночный": 50}
    size_dict = {0: 25, 1: 30, 2: 35}
    _price = None

    def __init__(self, filling, sauce=0, size=1, dough=0):
        self._size = size
        self._dough = dough
        self._sauce = sauce
        self._filling = filling
        self.__recalculate_price()
        self._isPrepared = False
        self._isCooked = False
        self._isCut = False

    @property
    def size(self):
        return self.size_dict[self._size]

    @size.setter
    def size(self, size):
        self._size = size
        self.__recalculate_price()

    @property
    def dough(self):
        return self.dough_dict[self._dough]

    @dough.setter
    def dough(self, dough):
        self._dough = dough

    @property
    def sauce(self):
        return self.sauce_dict[self._sauce]

    @sauce.setter
    def sauce(self, sauce):
        self._sauce = sauce
        self.__recalculate_price()

    @property
    def filling(self):
        return self._filling

    @filling.setter
    def filling(self, filling):
        self._filling = filling

    @property
    def price(self):
        return self._price

    def __recalculate_price(self):
        size = self._size
        if isinstance(self, PizzaPeperoni):
            self._price = PizzaPeperoni.price_list[size]
        elif isinstance(self, PizzaBBQ):
            self._price = PizzaBBQ.price_list[size]
        elif isinstance(self, PizzaSeaFood):
            self._price = PizzaSeaFood.price_list[size]
        self._price += self.sauce_price_dict.get(self.sauce_dict[self._sauce], 0)

    def prepare(self):
        self._isPrepared = True
        print("Все, что необходимо для пиццы, подготовлено!\n")

    def cook(self):
        self._isCooked = True
        print("Пицца приготовлена!\n")

    def cut(self):
        self._isCut = True
        print("Пицца нарезана!\n")

    @abstractmethod
    def bake(self):
        pass


class PizzaPeperoni(Pizza):
    price_list = [250, 300, 350]
    name = "Пицца 'Пеперони'"

    filling = ["Тесто для пиццы",
               "Сыр моцарелла",
               "Оливковое масло",
               "Сырокопченая колбаса",
               "Перец чили",
               "Помидоры в собственном соку",
               "Орегано",
               "Сушеный базилик",
               "Чеснок",
               "Сахар",
               "Соль",
               "Молотый черный перец"]

    def __init__(self, sauce=0, size=1, dough=0):
        super().__init__(self.filling, sauce, size, dough)

    def bake(self):
        print(self.name + " / " +
              self.dough + " тесто / " +
              self.sauce + " соуса - готовится 8 минут!")


class PizzaBBQ(Pizza):
    price_list = [300, 400, 500]
    name = "Пицца 'Барбекю'"

    filling = ["Тесто для пиццы",
               "Сыр моцарелла",
               "Оливковое масло",
               "Куриная грудка",
               "Перец чили",
               "Помидоры в собственном соку",
               "Соус Барбекю"
               "Сушеный базилик",
               "Чеснок",
               "Сахар",
               "Соль",
               "Молотый черный перец"]

    def __init__(self, sauce=0, size=1, dough=0):
        super().__init__(self.filling, sauce, size, dough)

    def bake(self):
        print(self.name + " / " +
              self.dough + " тесто / " +
              self.sauce + " соуса - готовится 9 минут!")


class PizzaSeaFood(Pizza):
    price_list = [350, 500, 650]
    name = "Пицца 'Дары Моря'"

    filling = ["Тесто для пиццы",
               "Сыр моцарелла",
               "Сливочное масло",
               "Креветки",
               "Мидии"
               "Перец сладкий",
               "Помидоры в собственном соку",
               "Оливки"
               "Чеснок",
               "Сахар",
               "Соль",
               "Молотый черный перец"]

    def __init__(self, sauce=0, size=1, dough=0):
        super().__init__(self.filling, sauce, size, dough)

    def bake(self):
        print(self.name + " / " +
              self.dough + " тесто / " +
              self.sauce + " соуса - готовится 10 минут!")
