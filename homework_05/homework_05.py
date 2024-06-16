# Задание 1.
print("\nЗадание 1.")


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() > 0:
            self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        new_task = (priority, task)

        index = 0
        while index < self.tasks.size() and new_task[0] > self.tasks.peek()[0]:
            index += 1

        self.tasks.items.insert(index, new_task)

    def remove_task(self, task):
        self.tasks.items = [t for t in self.tasks.items if t[1] != task]

    def info(self):
        priority_tasks = {}
        for priority, task in self.tasks.items:
            if priority not in priority_tasks:
                priority_tasks[priority] = [task]
            else:
                priority_tasks[priority].append(task)

        sorted_tasks = sorted(priority_tasks.items(), key=lambda x: x[0])

        result = []
        for priority, task_list in sorted_tasks:
            tasks_str = "; ".join(task_list)
            result.append(f"{priority} {tasks_str}")

        return "\n".join(result)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager.info(), "\n")

# Удаление задачи "помыть посуду"
manager.remove_task("помыть посуду")
print(manager.info())


# Задание 2.
print("\nЗадание 2.")


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        self.order_list = []

    @property
    def cache(self):
        if not self.order_list:
            return None
        key_to_get = self.order_list[-1]
        return key_to_get, self.cache_dict[key_to_get]

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            self.order_list.remove(key)
            del self.cache_dict[key]
        if len(self.cache_dict) >= self.capacity:
            oldest_key = self.order_list.pop(0)
            del self.cache_dict[oldest_key]
        self.cache_dict[key] = value
        self.order_list.append(key)

    def get(self, key):
        if key in self.cache_dict:
            self.order_list.remove(key)
            self.order_list.append(key)
            return self.cache_dict[key]
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key in self.order_list:
            print(f"{key} : {self.cache_dict[key]}")


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновлённый кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4


# Задание 3.
print("\nЗадание 3.")


def economizer(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@economizer
def fibonacci_counter(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_counter(n - 1) + fibonacci_counter(n - 2)


print(fibonacci_counter(9))


# Задание 4.
print("\nЗадание 4.")


class Cell:
    def __init__(self, number):
        self.number = number
        self.value = ' '

    def is_empty(self):
        return self.value == ' '

    def set_value(self, symbol):
        if self.is_empty():
            self.value = symbol
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        for i in range(0, 9, 3):
            row = [self.cells[i].value, self.cells[i + 1].value, self.cells[i + 2].value]
            print(f"| {' | '.join(row)} |")

    def is_full(self):
        return all(not cell.is_empty() for cell in self.cells)

    def check_win(self, symbol):
        for i in range(0, 9, 3):
            if all(self.cells[i + j].value == symbol for j in range(3)):
                return True
        for i in range(3):
            if all(self.cells[i + j * 3].value == symbol for j in range(3)):
                return True
        if self.cells[0].value == symbol and self.cells[4].value == symbol and self.cells[8].value == symbol:
            return True
        if self.cells[2].value == symbol and self.cells[4].value == symbol and self.cells[6].value == symbol:
            return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board, cell_number):
        if 1 <= cell_number <= 9:
            cell = board.cells[cell_number - 1]
            if cell.set_value(self.symbol):
                return True
        return False


def play_game():
    board = Board()
    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "O")
    current_player = player1

    while True:
        board.display()
        cell_number = int(input(f"\n{current_player.name}, выберите номер свободной клетки (1-9): "))
        if current_player.make_move(board, cell_number):
            if board.check_win(current_player.symbol):
                board.display()
                print(f"{current_player.name} выиграл.")
                break
            elif board.is_full():
                board.display()
                print("Ничья.")
                break
            else:
                current_player = player2 if current_player == player1 else player1
        else:
            print("Неверный ход. Попробуйте еще раз.")


play_game()
