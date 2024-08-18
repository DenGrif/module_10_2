# -*- coding: utf-8 -*-

import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(f"{self.name}, на нас напали")

        while enemies > 0:
            time.sleep(1)
            enemies -= self.power
            days += 1
            if enemies > 0:
                print(f"{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.")
            else:
                print(f"{self.name} одержал победу спустя {days} дней(дня)!")

# Создание обьектов класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# start потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Всё, битвы закончились!")


