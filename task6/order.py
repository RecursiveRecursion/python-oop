from exceptions import PizzaOverload, PizzaDiscount


class Order:
    _counter_order = 0
    __total = 0

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
        if len(self._order_list) > 10:
            raise PizzaOverload(len(self._order_list))
        self._price_order += pizza.price

    def complete(self):
        Order._counter_order -= 1

    def decline(self):
        Order._counter_order -= 1

    def get_total_price(self):
        current_total_price = self._price_order
        try:
            if len(self._order_list) > 4:
                raise PizzaDiscount
        except PizzaDiscount as e:
            print(e)
            current_total_price *= 0.8
        finally:
            self._price_order = current_total_price

    def __str__(self):
        return "Информация о заказе:\nНомер заказа: {}\nСписок заказа: {}\n" \
               "Общая стоимость заказа: {}".format(self._counter_order, self._order_list, self._price_order)