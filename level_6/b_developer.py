"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса Employee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self):
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float):
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float):
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float):
        employee.salary -= amount


class Developer(SuperAdminMixin, Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float, program_lang: str):
        super().__init__(name, surname, age, salary)
        self.program_lang = program_lang
    
    def get_info(self):
        return f'{super().get_info()} and the "{self.program_lang}" programming language'


if __name__ == '__main__':
    person = Developer('Steve', 'Miner', 34, 110250.25, 'Coal')
    print(person.get_info())
    person.increase_salary(person, 5000.2)
    print(person.get_info())
    person.decrease_salary(person, 3000.3)
    print(person.get_info())

