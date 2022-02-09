# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} go.'

    def stop(self):
        return f'\nThe {self.name} stop.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nYour speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return f'\nYour speed is too high! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            return f'\nYour speed is too high! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is correct'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town = TownCar('TownCar', 80, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('SportCar', 120, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('GarbageTruck', 40, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Police', 90, 'blue-white')
print('4:\n' + police.go(), police.show_speed(), police.turn('left'), police.turn('right'), police.turn('left'), police.turn('right'), police.stop())