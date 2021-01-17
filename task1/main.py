# Задание 1. Базовые возможности Python


# Запрашивает ввод чисел от пользователя.  Заканчивает ожидание ввода, когда пользователь вводит "done".
def enter_numbers(numbers):
    print("Введите произвольные числа (\"done\" для завершения ввода):")
    while True:
        num = input()
        if num == "done":
            break
        try:
            num = float(num)
            numbers.append(num)  # добавляет корректно введенные данные в список
        except ValueError:
            print("Ошибка: некорректный ввод.")
            continue


# Умножает все числа на 0.13 и сортирует список в порядке возрастания.
def modify_numbers(numbers):
    i = 0
    for num in numbers:
        num *= 0.13
        numbers[i] = num
        i += 1

    numbers.sort()


# Выводит список чисел на экран с округлением до двух знаков после запятой.
def print_numbers(numbers):
    print("Список чисел:")
    for num in numbers:
        print("{:.2f}".format(num))


# Сохраняет список чисел с округлением до двух знаков после запятой в файл.
def save_to_file(numbers):
    f = open("numbers.txt", "w")  # файл в формате .txt - универсальный текстовый формат
    for num in numbers:
        f.write("{:.2f}".format(num) + "\n")
    f.close()


# Функция точки входа в программу.
def main():
    numbers = []
    enter_numbers(numbers)
    modify_numbers(numbers)
    print_numbers(numbers)
    save_to_file(numbers)


# Точка входа в программу.
main()
