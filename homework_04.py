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


class Rectangle:
    def __init__(self, point_1, point_2):
        self.x1, self.y1, self.x2, self.y2 = point_1.get_x(), point_1.get_y(), point_2.get_x(), point_2.get_y()
        self.width = point_2.get_x() - point_1.get_x()
        self.height = point_2.get_y() - point_1.get_y()

    def get_s(self):
        return self.width * self.height

    def get_p(self):
        return (self.width + self.height)*2

    def contains(self, point):
        return True if self.x1 <= point.get_x() <= self.x2 and self.y1 <= point.get_y() <= self.y2 else False


p1 = Point(2, 3)
p2 = Point(4, 4)
p3 = Point(2, 5)

rect = Rectangle(p1, p2)
# print(rect.get_p(), rect.get_s())
# print(rect.contains(p3))


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

    def __add__(self, other):
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

