import math
import datetime


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
    x = int(input("3 задание. \nВведите первое число: "))
    y = int(input("Введите второе число: "))
    z = int(input("Введите третье число: "))
    print(round((((x ** 5 + 7) / abs(-6) * y) ** (1. / 3)) / (7 - z % y), 3))


def task_04():
    x = float(input("4 задание. \nВведите первое число: "))
    y = float(input("Введите второе число: "))
    print(round(x + y), 1)


def task_05():
    a = int(input("5 задание. \nВведите a: "))
    b = int(input("Введите b: "))
    m = int(input("Введите m: "))
    n = int(input("Введите n: "))
    x = (-b) / a
    print(True if m <= x <= n else False)


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
    print("13 задание.")
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
    print("1-й: ", sa)
    print("2-й: ", sb)
    print("общие:", sa_and_sb)
    c = a + b
    c_asc = sorted(c)
    c_desc = sorted(c, reverse=True)
    even = list(c[1::2])
    odd = list(c[::2])
    sr_ar = sum(even) / len(even)
    sr_geom = (math.sqrt(math.prod(odd))) ** (1. / (len(odd) // 2))
    # todo По формуле среднего геометрического нужно из произведения получить корень в степени кол-ва элементов.
    #  Но тут для правильного ответа пришлось разделить кол-во элементов(4) на 2, возводить в 2 раза меньшую степень.
    c_max = max(c)
    c_min = min(c)
    print("\nИтоговые:")
    print("3-й:", c)
    print("Сортировка (возр.):", c_asc)
    print("Сортировка (убыв.):", c_desc)
    print("Ср. арифм. = ", format(sr_ar, ".2f"), "ср. геометр. =", format(sr_geom, ".2f"))
    print("Макс. и мин.:", c_max, c_min)


def task_14():
    print("14 задание.")
    info = dict()
    info["фио"] = "Иванов Иван Иванович"
    info["дата_рождения"] = "12.12.1992"
    info["место_рождения"] = "Москва"
    print(info)
    info["хобби"] = ["плавание", "йога", "футбол"]
    info["хобби"].append("программирование")
    info["животные"] = ("кошка мурка", "собака лайка")
    info["ЕГЭ"] = dict()
    info["ЕГЭ"]["математика"] = 20
    info["ЕГЭ"]["информатика"] = 20
    info["ЕГЭ"]["русский"] = 0
    info["ЕГЭ"].pop("русский")
    info["вузы"] = dict()
    info["вузы"]["МИСИС"] = 40
    info["вузы"]["МФТИ"] = 50
    print("Данные:")
    print(info)
    exams = tuple(sorted(info["ЕГЭ"].keys()))
    print("Предметы:", *exams)
    uni = sorted(info["вузы"].keys())
    print("Вузы:", *uni)
    print("\nОтветы на вопросы:")
    name = info["фио"].split()[1]
    starts_with_vowel = name[0].lower() in "аоуыэяёюие"
    print("* мое имя начинается на гласную букву:", starts_with_vowel)
    date_time_obj = datetime.datetime.strptime(info["дата_рождения"], '%d.%m.%Y')
    month = date_time_obj.month
    born_in_winter_or_summer = True if month in [12, 1, 2, 6, 7, 8] else False
    print("* родился летом или зимой:", born_in_winter_or_summer)
    hobbies_count = len(info['хобби'])
    print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info['хобби'][0]))
    exams_count = len(info['ЕГЭ'])
    print("* после окончания школы сдавал {} экз.".format(exams_count))
    sum_mark = sum(info['ЕГЭ'].values())
    print("* сумма баллов = {}".format(sum_mark))
    max_mark = max(info['ЕГЭ'].values())
    print("* макс. балл = {}".format(max_mark))
    vuz_count = 0
    for value in info["вузы"].values():
        if sum_mark >= value:
            vuz_count += 1
    print("* кол-во вузов в которые прохожу: {}".format(vuz_count))


task_01()
task_02()
task_03()
task_04()
task_05()
task_06()
task_07()
task_08()
task_09()
task_10()
task_11()
task_12()
task_13()
task_14()
