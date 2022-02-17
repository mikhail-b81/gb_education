# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        num1 = self.num1 + other.num1
        num2 = self.num2 + other.num2
        return Numbers(num1, num2)

    def __mul__(self, other):
        num1 = (self.num1 * other.num1) - (self.num2 * other.num2)
        num2 = (self.num1 * other.num2) + (self.num2 * other.num1)
        return Numbers(num1, num2)

    def __str__(self):
        return f'{self.num1} + {self.num2} * i'



z1 = Numbers(4, 7)
z2 = Numbers(2, 5)
z3 = z1 + z2
z4 = z1 * z2

print(f'z1 = {z1}')
print(f'z2 = {z2}')
print(f'z1 + z2 = {z3}')
print(f'z1 * z2 = {z4}')