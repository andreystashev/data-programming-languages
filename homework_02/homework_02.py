def task_01():
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]

    a += b
    five = a.count(5)
    for _ in range(five):
        a.remove(5)
    a += c
    three = a.count(3)

    print(five, three, a, sep='\n')


def task_02():
    a = list(range(160, 176, 2))
    b = list(range(162, 180, 3))
    print(sorted(a + b))


def task_03():
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
            ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    name = input("Введите деталь: ")
    count = 0
    price = 0
    for i in shop:
        if i[0] == name:
            count += 1
            price += i[1]
    print(f"Название детали: {name} \nКол-во деталей — {count} \nОбщая стоимость — {price}")


def task_04():
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    while True:
        print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
        people_changing = input("Гость пришёл или ушёл? ")
        if people_changing == "пришёл":
            guest = input("Имя гостя: ")
            if len(guests) < 6:
                guests.append(guest)
                print(f"Привет, {guest}")
            else:
                print(f"Прости, {guest}, но мест нет.")
        elif people_changing == "ушёл":
            guest = input("Имя гостя: ")
            guests.remove(guest)
            print(f"Пока, {guest}")
        else:
            print("Вечеринка закончилась, все легли спать.")
            break


def task_05():
    violator_songs = [
        ['World in My Eyes', 4, 86],
        ['Sweetest Perfection', 4, 43],
        ['Personal Jesus', 4, 56],
        ['Halo', 4, 9],
        ['Waiting for the Night', 6, 7],
        ['Enjoy the Silence', 4, 20],
        ['Policy of Truth', 4, 76],
        ['Blue Dress', 4, 29],
        ['Clean', 5, 83]
    ]
    minutes, seconds = 0, 0
    for i in range(1, 1 + int(input("Сколько песен выбрать? "))):
        song = input(f"Название {i}-й песни: ")
        for j in violator_songs:
            if song == j[0]:
                minutes += j[1]
                seconds += j[2]
                break
    minutes += seconds // 100
    seconds = seconds % 100
    print(f"Общее время звучания песен: {minutes},{seconds} минуты")


def task_06():
    a, b = list(), list()
    for i in range(1, 4):
        a.append(int(input(f"Введите {i}-е число для первого списка: ")))
    for i in range(1, 8):
        b.append(int(input(f"Введите {i}-е число для второго списка: ")))
    print(f"Первый список:{a} \nВторой список:{b} \nНовый первый список с уникальными элементами:{list(set(a + b))}")


def task_07():
    a, b = list(), list()
    for i in range(1, 1 + int(input("Кол-во коньков: "))):
        a.append(int(input(f"Размер {i}-й пары: ")))
    for i in range(1, 1 + int(input("Кол-во людей: "))):
        b.append(int(input(f"Размер ноги {i}-го человека: ")))
    count = 0
    for i in b:
        if i in a:
            a.remove(i)
            count += 1
    print("Наибольшее кол-во людей, которые могут взять ролики:", count)


def task_08():
    people_count = int(input("Кол-во человек: "))
    step = int(input("Какое число в считалке? "))
    people = [*range(1, 1 + people_count)]
    pointer = 0
    offset = 1
    while True:
        print("\nТекущий круг людей:", people)
        print("Начало счёта с номера", people[pointer % len(people)])
        pointer += step-offset
        offset += 1
        print("Выбывает человек под номером", people[pointer % len(people)])
        people.remove(people[pointer % len(people)])
        if len(people) < 2:
            print("Остался человек под номером", people[0])
            break


def task_09():
    a = dict()
    friends = int(input("Кол-во друзей: "))
    taxes = int(input("Долговых расписок: "))
    for i in range(1, friends + 1):
        a[i] = 0
    for i in range(1, taxes + 1):
        print(f"\n{i}-я расписка")
        creditor = int(input("Кому: "))
        debtor = int(input("От кого: "))
        tax = int(input("Сколько: "))
        a[creditor] -= tax
        a[debtor] += tax
    print("Баланс друзей:")
    for friend, money in a.items():
        print(f"{friend} : {money}")


def task_10():
    a = list()
    for i in range(int(input("Кол-во чисел: "))):
        a.append(int(input(f"Число: ")))
    b = a.copy()
    b.reverse()
    for i in range(len(a)):
        if b[i] != a[len(a) - 1]:
            b = b[i:]
            break
    print(f"Последовательность: {a} \nНужно приписать чисел: {len(b)} \nСами числа: {b}")


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
