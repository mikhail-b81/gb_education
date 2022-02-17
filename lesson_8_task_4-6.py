# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class TechnicStore:

    def __init__(self, title, quantity, price, *args):
        self.title = title
        self.quantity = quantity
        self.price = price
        self.store = []
        self.new_title = {'Название: ': self.title, 'Количество: ': self.quantity, 'Стоимость: ': self.price}

    def __str__(self):
        return f'{self.title} стоимость {self.price} количество {self.quantity}'

    def reception(self):
        try:
            new_title = input(f'Введите наименование новой аппаратуры ')
            new_title_quantity = int(input(f'Введите количество '))
            new_title_price = int(input(f'Введите цену за штуку '))
            new_position = {'Название: ': new_title, 'Количество: ': new_title_quantity, 'Стоимость: ': new_title_price}
            # self.new_title.update(unique)
            self.store.append(new_position)

            print(f'Список заведенных позиций:\n {self.store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Завершить - stop, Продолжить - Enter')
        q = input('?')
        if q == 'stop':
            print(f'Все заведенные на склад позиции\n {self.store}')
            return f'Выход'
        else:
            return TechnicStore.reception(self)


class Printer(TechnicStore):
    def report_print(self):
        count_new_printers = len(self.store)
        print(
            f'{"-" * 50}\nОтчет по поступлению новых принтеров\nНа склад поступило {count_new_printers} новых поставки\n{"-" * 50}')


class Scan(TechnicStore):
    def report_scan(self):
        count_new_printers = len(self.store)
        print(
            f'{"-" * 50}\nОтчет по поступлению новых сканеров\nНа склад поступило {count_new_printers} новых поставки\n{"-" * 50}')


class Xerox(TechnicStore):
    def report_xerox(self):
        count_new_printers = len(self.store)
        print(
            f'{"-" * 50}\nОтчет по поступлению новых ксероксов\nНа склад поступило {count_new_printers} новых поставки\n{"-" * 50}')


unit_print = Printer('hp', 1, 2000, 5)
unit_scan = Scan('Canon', 2, 1200, 5)
unit_xer = Xerox('Xerox', 4, 1500, 1)


print(unit_print.reception())
print(unit_print.report_print())

print(unit_scan.reception())
print(unit_scan.report_scan())

print(unit_xer.reception())
print(unit_xer.report_xerox())


