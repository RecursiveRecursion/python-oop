import time


class HandoutMeta(type):
    def __new__(cls, name, bases, dct):
        dct["location_of_pickup"] = dct["locationOfPickupPoint"]
        dct.pop("locationOfPickupPoint")
        print(dct)
        return type(name, bases, dct)


def with_stats(method):
    def get_stats(self, takeout):
        print("### Инициализируем задачу {} ###".format(method.__name__))
        start = time.time()
        method(self, takeout)
        end = time.time()
        print("### Завершили задачу '{}' за {:.2f} сек. ###".format(method.__name__, end - start))
    return get_stats


class Handout(metaclass=HandoutMeta):
    locationOfPickupPoint = "рядом с окном номер четыре"

    @with_stats
    def pack(self, takeout):
        if takeout:
            print("Упаковываем {} в коробку...".format(self.name))
            time.sleep(2)
        else:
            print("Выкладываем {} на тарелку...".format(self.name))
            time.sleep(1)
