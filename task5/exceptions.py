class PizzaOverload(Exception):
    def __init__(self, pizza_count):
        self.pizza_count = pizza_count

    def __str__(self):
        return "10 пицц - это максимум (вы пытались заказать {})".format(self.pizza_count)


class PizzaDiscount(Exception):
    def __str__(self):
        return "Поздравляем! В вашем заказе 5 пицц, поэтому вы получаете 20% скидку!"
