# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
#
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, date):
        self.date = date    # str '27-05-1999'


    @classmethod
    def extract_data(cls, date):
        return [int(i) for i in (date.split("-"))]


    @staticmethod
    def valid_num(date):
        day = Date.extract_data(date)[0]
        month = Date.extract_data(date)[1]
        year = Date.extract_data(date)[2]

        if year <= 0:
            print('Ошибка: некорректный год')
        elif month <= 0 or month >= 12:
            print('Ошибка: некорретный месяц')
        elif day <= 0 or day > 31:
            print('Ошибка: некорректный день')
        elif month in [4,6,9,11] and day > 30:
            print('Ошибка: некорректный день')
        elif year % 4 == 0 and year % 100 != 0 and month == 2 and day > 29: # Февраль, високосный год
            print('Ошибка: некорректный день')
        elif year % 4 != 0 and month == 2 and day > 28:
            print('Ошибка: некорректный день')
        else:
            print(f'Дата прошла проверку:\nДень: {day}\nМесяц: {month}\nГод: {year}')


b = Date
# b.valid_num('29-02-2018')   # не високосный год
# b.valid_num('29-02-2020')   # високосный год
# b.valid_num('31-09-2018')
# b.valid_num('20-15-2010')
b.valid_num('19-04-1999')


