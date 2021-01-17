import os

import pizza
import order
from handout import Handout


class Terminal:
    menu_dict = {1: pizza.PizzaPeperoni,
                 2: pizza.PizzaBBQ,
                 3: pizza.PizzaSeaFood}
    order_current = None
    __is_menu_showed = None

    def __init__(self):
        self.order_current = None
        self.__is_menu_showed = False

    @property
    def is_menu_showed(self):
        return self.__is_menu_showed

    @is_menu_showed.setter
    def is_menu_showed(self, is_showed):
        self.__is_menu_showed = is_showed
        if is_showed:
            self.__show_menu()

    def __show_menu(self):
        value = ""
        while value != "-1":
            os.system("cls")
            print("Меню:")
            for position in self.menu_dict:
                print(f"{position}. {self.menu_dict[position].name}")
            print("\n 0. Сделать заказ")
            print("-1. Завершить работу")
            value = input()
            if value == "0":
                self.make_order()

    def make_order(self):
        print("Заказ с собой? y/n")
        option = 0
        self.order_current = order.Order(True) if input() == ("y" or "Y") else order.Order()
        while option != "+" and option != "-":
            os.system("cls")
            option = input("Введите номер пиццы из меню. Для подтверждения заказа введите '+', "
                           "для отмены -- '-': \n")
            if option.isdecimal():
                option = int(option)
                if 0 < option <= len(self.menu_dict):
                    ordered_pizza = self.menu_dict.get(option, 1)
                    ordered_pizza = ordered_pizza()
                    self.order_current.add(ordered_pizza)
                    ordered_pizza.bake()
                    ordered_pizza.pack(self.order_current.takeout)
                else:
                    print("В меню нет такой позиции!")
            else:
                if option == "+" or option == "-":
                    os.system("cls")
                    if option == "+":
                        print(self.order_current)
                        print("--------------------------")
                        print("Пройдите на выдачу.")
                        print("Вы можете забрать свой заказ " + Handout.location_of_pickup)
                    else:
                        self.order_current.decline()
                        print("Заказ отменен.")
                    input("\nНажмите 'Enter'\n")
                else:
                    print("Некорректная опция!")
