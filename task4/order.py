class Order:
    _counter_order = 0

    def __init__(self, takeout=False):
        self._order_list = []
        Order._counter_order += 1
        self._price_order = 0
        self.takeout = takeout

    @property
    def counter_order(self):
        return Order._counter_order

    @property
    def pizzas_ordered(self):
        return self._order_list

    @property
    def price_order(self):
        return self._price_order

    def add(self, pizza):
        self._order_list.append(pizza.name)
        self._price_order += pizza.price

    def complete(self):
        Order._counter_order -= 1

    def decline(self):
        Order._counter_order -= 1

    def __str__(self):
        return "Информация о заказе:\nНомер заказа: {}\nСписок заказа: {}\n" \
               "Общая стоимость заказа: {}".format(self._counter_order, self._order_list, self._price_order)