"""ТЗ для проекта “CRUD”
Цель проекта: реализовать систему управления задачами
Требования к заданию:
1. Создание класса Task:
• Класс должен иметь следующие атрибуты: название задачи, описание, статус (выполнено/не выполнено), дата создания.
• Класс должен иметь методы:
• mark_as_done: для установки статуса задачи "выполнено".
• mark_as_undone: для установки статуса задачи "не выполнено".
• edit_description: для редактирования описания задачи.
• __str__: магический метод, возвращающий строковое представление задачи.

2. Создание класса TaskList:
• Класс должен иметь следующие атрибуты: список задач.
• Класс должен иметь методы:
• create_task: для добавления новой задачи в список.
• get_task: для получения задачи по индексу.
• remove_task: для удаления задачи из списка.
• get_all_tasks: для получения списка всех задач.
• __len__: магический метод, возвращающий количество задач в списке.
3. Создание декоратора log_activity:
• Декоратор должен выводить информацию о выполненных методах классов Task и TaskList.
• Информация должна содержать дату и время выполнения метода и его аргументы.

Extra функционал:
● Создание интерфейса в терминале, чтобы пользователю можно было взаимодействовать с крадом через терминал. (доп баллы)
● Сохранение данных в базу данных (json / airtable(доп баллы))
Требования к проекту:
- код должен соответствовать PEP8
- при использовании каких-либо библиотек, укажите их в файле requirements.txt
- при выполнении кода не должно возникать ошибок
- свой проект нужно закинуть в GitHub"""


import datetime


def log_activity(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        formatted_args = ', '.join([repr(arg) for arg in args])
        formatted_kwargs = ', '.join([f"{key}={repr(value)}" for key, value in kwargs.items()])
        arguments = ', '.join(filter(None, [formatted_args, formatted_kwargs]))

        result = func(*args, **kwargs)
        print(f"[{timestamp}] Calling method {func.__name__}({arguments})")
        return result

    return wrapper


class Task:
    def __init__(self, title, description, status="not done"):
        self.title = title
        self.description = description
        self.status = status
        self.creation_date = datetime.datetime.now().strftime("%Y-%m-%d")

    @log_activity
    def mark_as_done(self):
        self.status = "done"

    @log_activity
    def mark_as_undone(self):
        self.status = "not done"

    @log_activity
    def edit_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nStatus: {self.status}\nCreation Date: {self.creation_date}"


class TaskList:
    def __init__(self):
        self.tasks = []

    @log_activity
    def create_task(self, task):
        self.tasks.append(task)

    @log_activity
    def mark_task_as_done(self, task):
        task.mark_as_done()

    @log_activity
    def mark_task_as_undone(self, task):
        task.mark_as_undone()

    @log_activity
    def edit_task_description(self, task, new_description):
        task.edit_description(new_description)

    @log_activity
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task successfully removed.")
        else:
            print("Task not found in the list.")

    @log_activity
    def get_all_tasks(self):
        return self.tasks

    def __len__(self):
        return len(self.tasks)


task_list = TaskList()

task1 = Task("Study", "Complete assignment on the platform")
task2 = Task("Watch videos", "Watch videos on YouTube")

task_list.create_task(task1)
task_list.create_task(task2)

task_list.mark_task_as_done(task1)
task_list.edit_task_description(task2, "Pick up delivery")

all_tasks = task_list.get_all_tasks()
for task in all_tasks:
    print(task)
    print()

print(f"Number of tasks: {len(task_list)}")

