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

