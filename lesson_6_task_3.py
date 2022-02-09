# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return 'Employee name: ' + self.name + ' ' + self.surname

    def get_total_income(self):
        return '\nEmployee income: ' + str(self._income["wage"] + self._income["bonus"]) + '\n'


employee_one = Position('Mikhail', 'Mikhailov', 'worker', '100000', '50000')
print(employee_one.get_full_name(), employee_one.get_total_income())

employee_two = Position('Ivan', 'Ivanov', 'boss', '200000', '100000')
print(employee_two.get_full_name(), employee_two.get_total_income())

employee_three = Position('Andrey', 'Andreev', 'intern', '25000', '0')
print(employee_three.get_full_name(), employee_three.get_total_income())
