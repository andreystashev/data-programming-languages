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



# def task_03():
#     x = int(input("2 задание. \nВведите первое число: "))
#     y = int(input("Введите второе число: "))
#     z = int(input("Введите третье число: "))
#     math.sqrt
#     print("Ответ: ", n * (n + 1) // 2, end="\n\n")


def task_04():
    pass


def task_05():
    pass


def task_06():
    pass


def task_07():
    n1 = int(input("7 задание. \nВведите двузначное число: "))
    n2 = int(input("Введите трехзначное число: "))
    print(f"Первое число. Сумма: {n1 // 10 + n1 % 10}. Произведение: {n1 // 10 * (n1 % 10)}\n"
          f"Второе число. Сумма: {n2 // 100 + n2 // 10 % 10 + n2 % 10}. "
          f"Произведение: {n2 // 100 * (n2 // 10 % 10) * (n2 % 10)}")


def task_08():
    pass


def task_09():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(a, b)
    a = str(a)+" "+str(b)
    b = int(a.split()[0])
    a = int(a.split()[1])
    print(a, b)


def task_10():
    command = input()
    print(command, "- чемпион!")
    print('-' * len(command))
    command = command.lower()
    print(f"Длина {len(command)}\n"
          f"Наличие 'п': {'п' in command}\n"
          f"Повторы 'а': {command.count('а')}\n")


def task_11():
    state = input("Введите государство: ")
    capital = input("Введите столицу: ")
    print(f"Государство - {state}, столица - {capital}\n")


def task_12():
    word = "объектно-ориентированный"
    print(f"{word[:6]}\n{word[9:17]}\n{word[14:17]}\n"
          f"{word[4] + word[0] + word[5]}\n{word[10] + word[12:15] + word[19]}\n")


def task_13():
    pass


def task_14():
    pass


task_01()
task_02()
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
# task_13()
# task_14()