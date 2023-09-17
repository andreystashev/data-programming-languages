import datetime


def task_01():
    pass


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
        if char not in statistic.keys():
            statistic[char] = 1
        else:
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
    pass


def task_07():
    line = input("Введите строку: ")
    for i in range(len(line) // 2):
        if line[i] != line[len(line) - 1 - i]:
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
    pass


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


task_02()
