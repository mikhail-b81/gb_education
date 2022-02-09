# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time

class TrafficLight:
    _color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        count_switch = 0
        while count_switch != 3:
            print(f'\nСейчас горит {TrafficLight._color[count_switch]} свет')
            if count_switch == 0:
                for i in range(7,0,-1):
                    print(i, end='')
                    time.sleep(1)
            elif count_switch == 1:
                for i in range(3, 0, -1):
                    print(i, end='')
                    time.sleep(1)
            elif count_switch == 2:
                for i in range(8, 0, -1):
                    print(i, end='')
                    time.sleep(1)
            count_switch += 1


t = TrafficLight()

count_work = int(input('Сколько раз выполнить работу светофора: '))
for i in range(count_work):
    t.running()
    print('\n')
    print('-'*10)
