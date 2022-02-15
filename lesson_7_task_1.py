# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix():
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        s = ""
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                s += str(self.matr[i][j])+' '
            s += '\n'
        return s

    def __add__(self, other):
        num_list = []
        for i in range(len(self.matr)):
            row_list = []
            for j in range(len(self.matr[i])):
                new_obj = self.matr[i][j] + other.matr[i][j]
                row_list.append(new_obj)
            num_list.append(row_list)
        return Matrix(num_list)


a = Matrix([[10,-2,33,44,100],[-99,15,63,65,10]])
print(a)

b = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(b)

c = Matrix([[10,20,30],[40,50,60],[70,80,90]])
print(c + b)

