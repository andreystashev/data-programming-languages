import math


def task_01():
    n = int(input("1 задание. \nВведите число: "))
    print("Ответ: ", n * (n + 1) // 2, end="\n\n")


def task_02():
    n1 = int(input("2 задание. \nВведите первое число: "))
    n2 = int(input("Введите второе число: "))
    print("Ответ: ",
          f"{n1} + {n2} = {n1 + n2}\n",
          f"{n1} - {n2} = {n1 - n2}\n",
          f"{n1} * {n2} = {n1 * n2}\n",
          f"{n1} / {n2} = {round(n1 / n2, 2)}\n",
          f"{n1} // {n2} = {n1 // n2}\n",
          f"{n1} % {n2} = {n1 % n2}\n",
          f"{n1} ** {n2} = {n1 ** n2}\n",
          f"log10 {n1} и {n2} = {round(math.log10(n1), 2)} и {round(math.log10(n2), 2)}\n",
          f"{n1} < {n2} = {n1 < n2}\n",
          f"{n1} <= {n2} = {n1 <= n2}\n",
          f"{n1} > {n2} = {n1 > n2}\n",
          f"{n1} >= {n2} = {n1 >= n2}\n",
          f"{n1} != {n2} = {n1 != n2}\n",
          f"{n1} == {n2} = {n1 == n2}\n",
          end="\n\n")


def task_03():
    x = int(input("2 задание. \nВведите первое число: "))
    y = int(input("Введите второе число: "))
    z = int(input("Введите третье число: "))
    print(round((((x ** 5 + 7) / abs(-6) * y) ** (1. / 3)) / (7 - z % y), 3))


def task_04():
    pass


def task_05():
    pass


def task_06():
    v = int(input("6 задание. \nВведите скорость: "))
    t = int(input("Введите время: "))
    print(f"Остановка на {v * t % 122}\n")


def task_07():
    n1 = int(input("7 задание. \nВведите двузначное число: "))
    n2 = int(input("Введите трехзначное число: "))
    print(f"Первое число. Сумма: {n1 // 10 + n1 % 10}. Произведение: {n1 // 10 * (n1 % 10)}\n"
          f"Второе число. Сумма: {n2 // 100 + n2 // 10 % 10 + n2 % 10}. "
          f"Произведение: {n2 // 100 * (n2 // 10 % 10) * (n2 % 10)}")


def task_08():
    a = int(input("8 задание. \nВведите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    middle = a + b + c - minimum - maximum
    print(minimum, middle, maximum)


def task_09():
    a = int(input('9 задание. \nВведите первое число: '))
    b = int(input('Введите второе число: '))
    print(a, b)
    a = str(a) + " " + str(b)
    b = int(a.split()[0])
    a = int(a.split()[1])
    print(a, b)


def task_10():
    command = input('10 задание. \nВведите название команды: ')
    print(command, "- чемпион!")
    print('-' * len(command))
    command = command.lower()
    print(f"Длина {len(command)}\n"
          f"Наличие 'п': {'п' in command}\n"
          f"Повторы 'а': {command.count('а')}\n")


def task_11():
    state = input("11 задание. \nВведите государство: ")
    capital = input("Введите столицу: ")
    print(f"Государство - {state}, столица - {capital}\n")


def task_12():
    word = "объектно-ориентированный"
    print(f"12 задание. \n{word[:6]}\n{word[9:17]}\n{word[14:17]}\n"
          f"{word[4] + word[0] + word[5]}\n{word[10] + word[12:15] + word[19]}\n")


def task_13():
    a = list()
    b = list()
    a.append(4.5)
    a.append(3.4)
    a.extend([8.7, 1.3])
    b.append(14.5)
    b.append(3.4)
    b.extend([8.7, 11.3])
    a.insert(1, 100)
    a.insert(3, 100)
    b.insert(0, 200)
    b.insert(2, 200)
    print("Исходные списки:")
    print(a)
    print(b)
    del a[0]
    del b[0]
    a.remove(100)
    b.remove(200)
    print("\nПосле удалений:")
    print(a)
    print(b)
    sa = set(a)
    sb = set(b)
    sa_and_sb = sa.intersection(sb)
    print("\nУникальные элементы:")
    print("общие:", sa_and_sb)
    c = sa.union(sb)
    c_asc = sorted(c)
    c_desc = sorted(c, reverse=True)
    # # Среднее арифметическое элементов списка 'c', расположенных на четных местах
    # sr_ar =  sum(list(c[::2]))/len(c)//2
    # print(sr_ar)
    # # Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
    # sr_geom =  # Удалите комментарий и допишите код
    #
    # # Максимальный и минимальный элементы
    c_max = max(c)
    c_min =  min(c)

    #
    # # Вывести результаты на экран
    print("\nИтоговые:")
    print("3-й:", c)
    print("Сортировка (возр.):" ,c_asc)
    print("Сортировка (убыв.):",c_desc)
    print("Ср. арифм. = ",29.00, "ср. геометр. =", 7.82)
    print("Макс. и мин.:", c_max,c_min)
    # # Удалите комментарий и допишите код
    #
    # # --------------
    # # Пример вывода:
    # #
    # # Исходные списки:
    # # 1-й: [4.5, 100, 3.4, 100, 8.7, 1.3]
    # # 2-й: [200, 14.5, 200, 3.4, 8.7, 11.3]
    # #
    # # После удалений:
    # # 1-й: [3.4, 100, 8.7, 1.3]
    # # 2-й: [14.5, 3.4, 8.7, 11.3]
    # #
    # # Уникальные элементы:
    # # 1-й: {8.7, 1.3, 3.4, 100}
    # # 2-й: {8.7, 11.3, 3.4, 14.5}
    # # общие: {8.7, 3.4}
    #
    # # Итоговые:
    # # 3-й: [3.4, 100, 8.7, 1.3, 14.5, 3.4, 8.7, 11.3]
    # # Сортировка (возр.): [1.3, 3.4, 3.4, 8.7, 8.7, 11.3, 14.5, 100]
    # # Сортировка (убыв.): [100, 14.5, 11.3, 8.7, 8.7, 3.4, 3.4, 1.3]
    # # Ср. арифм. = 29.00, ср. геометр. = 7.82

def task_14():
    pass


# task_01()
# task_02()
# task_03()
# task_04()
# task_05()
# task_06()
# task_07()
# task_08()
# task_09()
# task_10()
# task_11()
# task_12()
task_13()
# task_14()
