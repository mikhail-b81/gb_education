# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        material_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна длинной {self._length} метров и шириной {self._width} метров неободимо {round(material_mass)} тонн асфальта')


road_length = int(input('Введите длинну проектиркемой дороги (в метрах): '))
road_width = int(input('Введите ширину проектиркемой дороги (в метрах): '))
r = Road(road_length, road_width)
r.asphalt_mass()


e = Road(10000, 50)
e.asphalt_mass()