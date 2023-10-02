import time

# Упражнение 1.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        print(self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

# Упражнение 2.


class Rectangle:
    def __init__(self, point_1, point_2):
        self.x1, self.y1, self.x2, self.y2 = point_1.get_x(), point_1.get_y(), point_2.get_x(), point_2.get_y()
        self.width = point_2.get_x() - point_1.get_x()
        self.height = point_2.get_y() - point_1.get_y()

    def get_s(self):
        return self.width * self.height

    def get_p(self):
        return (self.width + self.height)*2

    def contains(self, point):  # Упражнение 3.
        return True if self.x1 <= point.get_x() <= self.x2 and self.y1 <= point.get_y() <= self.y2 else False


p1 = Point(2, 3)
p2 = Point(4, 4)
p3 = Point(2, 5)

rect = Rectangle(p1, p2)
# print(rect.get_p(), rect.get_s())
# print(rect.contains(p3))


# Упражнение 4.


class Counter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        if self.counter > 0:
            self.counter -= 1

    def get_counter(self):
        return self.counter

# Упражнение 5.


class Watch:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_hour(self):
        self.hour += 1
        if self.hour == 24:
            self.hour = 0

    def add_minute(self):
        self.minute += 1
        if self.minute >= 60:
            self.add_hour()
            self.minute -= 60

    def add_second(self):
        self.second += 1
        if self.second >= 60:
            self.add_minute()
            self.second -= 60

    def __add__(self, other):   # Упражнение 6.
        self.second += other.second
        if self.second > 59:
            self.second -= 60
            self.add_minute()

        self.minute += other.minute
        if self.minute > 59:
            self.minute -= 60
            self.add_hour()

        self.hour += other.hour

    def info(self):
        print(self.hour, self.minute, self.second)


w = Watch(11, 59, 20)
w.info()
w2 = Watch(12, 1, 50)

w+w2
w.info()


# Упражнение 7.


class Grass:
    def __init__(self, nutritional):
        self.nutritional = nutritional


class Animal:
    def __init__(self, name):
        self.stomach = 50
        self.name = name

    def live(self, grass):
        if self.stomach < 50:
            while self.stomach < 200:
                time.sleep(0.2)
                self.eat(grass)
            print(f"Животное {self.name} наелось.")
        else:
            self.wait()

    def wait(self):
        self.stomach -= 20
        print(f"{self.name} гуляет. Наполненность желудка {self.stomach}.")

    def eat(self, grass):
        self.stomach += grass.nutritional
        print(f"{self.name} eст. Наполненность желудка {self.stomach}.")


def task_07():
    field = Grass(25)
    cow = Animal("Корова")
    while True:
        time.sleep(1)
        cow.live(field)

# task_07()


class Storm:
    def __init__(self):
        print("Storm")


class Dust:
    def __init__(self):
        print("Dust")


class Lightning:
    def __init__(self):
        print("Lightning")


class Lava:
    def __init__(self):
        print("Lava")


class Mud:
    def __init__(self):
        print("Mud")


class Steam:
    def __init__(self):
        print("Steam")



class Earth:
    def __init__(self):
        print("Earth")

    def __add__(self, other):
        # print("add work",other)
        # return Lava()
        if other is Fire:
            print("Fire")
        #     return Lava()
        # if other == Water:
        #     return Mud()




class Fire:
    def __init__(self):
        print("Fire")


class Water:
    def __init__(self):
        print("Water")


class Air:
    def __init__(self):
        print("Air")

e = Earth()
f = Fire()
w = Water()

print(e+f)
print(e+w)