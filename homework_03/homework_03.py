import datetime


def task_01():
    massive = [12, 9]
    minimum = min(massive)
    while minimum > 0:
        nok = True
        for i in massive:
            if i / minimum != i // minimum:
                nok = False
        if nok:
            print(minimum, "НОК")
            break
        minimum -= 1

    maximum = max(massive)
    while True:
        nod = True
        for i in massive:
            if maximum % i != 0:
                nod = False
        if nod:
            print(maximum, "НОД")
            break
        maximum += 1


def task_02():
    counter = 0
    nums = "0123456789"

    strings = int(input("Введите кол-во предложений: "))
    for i in range(strings):
        string = input("Введите предложение: ")
        for char in string:
            if char in nums:
                counter += 1
                break
    print("Кол-во предложений, содержащих цифру:", counter)


def task_03():
    line = input("Введите строку: ")
    symbol = input("Введите символ: ")
    line_length = len(line) + 2
    print(f"{symbol * line_length}\n{symbol}{line}{symbol}\n{symbol * line_length}")


def task_04():
    line = input("Введите строку: ").lower()
    statistic = dict()
    for char in line:
        statistic.setdefault(char, 0)
        statistic[char] += 1
    for key, value in statistic.items():
        print(f"'{key}'", "=", value)


def task_05():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    line = input("Введите строку: ")
    shift = int(input("Введите сдвиг: "))
    encode_line = ""
    for char in line:
        position = alphabet.find(char.lower())
        lower = char.islower()
        if position != -1:
            encode_line += alphabet[(position + shift) % 33] if lower else alphabet[(position + shift) % 33].upper()
        else:
            encode_line += char
    print(encode_line)

    decode_line = ""
    for char in encode_line:
        position = alphabet.find(char.lower())
        lower = char.islower()
        if position != -1:
            decode_line += alphabet[(position - shift) % 33] if lower else alphabet[(position - shift) % 33].upper()
        else:
            decode_line += char
    print(decode_line)


def task_06():
    def foo(*nums):
        minus, plus = list(), list()
        for i in sorted(nums):
            if i < 0:
                minus.append(i)
            else:
                plus.append(i)
        minus.sort(reverse=True)
        return minus, plus

    print(foo(1, 2, 3, 4, 5, 0, -1, -4, -5))


def task_07():
    line = input("Введите строку: ")
    for i in range(len(line) // 2):
        if line[i] != line[- 1 - i]:
            print("Не палиндром")
            break
    else:
        print("Палиндром")


def task_08():
    start = -1
    end = 100
    counter = 0
    while True:
        counter += 1
        middle = (end + start + 1) // 2
        result = int(input(f"Твое число равно (1), меньше (3) или больше (2), чем число {middle}?\n"))

        if result == 1:
            break
        elif result == 2:
            start = middle
        elif result == 3:
            end = middle
    print(f"Угадано за {counter} попыток.")


def task_09():
    converter = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C",
                 13: "D", 14: "E", 15: "F"}

    def from_ten(number, system):
        result = ""
        while number > 0:
            result += converter[number % system]
            number //= system
        return result[::-1]

    def to_ten(number, system):
        number = number[::-1]
        result = 0
        mult = 0
        for char in number:
            for key, value in converter.items():
                if char == value:
                    result += (key * pow(system, mult))
                    break
            mult += 1
        return result

    while True:
        print("Поддерживаются системы счисления не больше 16 и не меньше 2")
        system_from = int(input("Какая исходная система счисления? :"))
        system_to = int(input("В какую переводим? :"))
        if 1 < system_from < 17 and 1 < system_to < 17:
            break

    while True:
        num = input("Какое число? :")
        is_correct = True
        for i in num:
            for key, value in converter.items():
                if value == i and key > system_from:
                    is_correct = False
                    print("Число содержит символы, отсутствующие в выбранной системе счисления")
        if is_correct:
            break

    print("Результат:", from_ten(to_ten(num, system_from), system_to))


def task_10():
    def magic_check(day: int, month: int, year: int):
        return day * month == year % 100

    counter = 0
    for y in range(1900, 2000):
        for m in range(1, 13):
            for d in range(1, 32):
                try:
                    date = datetime.date(y, m, d)
                except ValueError:
                    continue
                if magic_check(date.day, date.month, date.year):
                    counter += 1
                    print(f"{counter})", date.strftime("%d.%m.%Y"))


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
