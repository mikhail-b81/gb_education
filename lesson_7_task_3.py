# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    def __init__(self, slots):
        self.slots = slots

    def __add__(self, other):
        return Cell(self.slots + other.slots)

    def __sub__(self, other):
        deduct = self.slots - other.slots
        if deduct <= 0:
            return f'Ошибка вычитания'
        else:
            return Cell(deduct)

    def __mul__(self, other):
        return Cell(self.slots * other.slots)

    def __truediv__(self, other):
        return Cell(self.slots // other.slots)

    def make_order(self, quantity):
        s = ""
        for cl in range(self.slots // quantity):
            s += '*' * quantity + '\n'
        s += '*' * (self.slots % quantity) + '\n'
        return s

    def __str__(self):
        return f'{self.slots}'

cell = Cell(22)
print(cell.make_order(8))

cell2 = Cell(15)
print(cell2.make_order(5))

print(cell - cell2)
print(cell + cell2)
print(cell * cell2)
print(cell / cell2)
print(cell2 - cell)
