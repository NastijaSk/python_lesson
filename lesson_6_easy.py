#coding:utf-8
__author__ = 'ASUS'

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда

class Car:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        print(self.name, 'машина поехала')

    def stop(self):
        print(self.name, 'машина остановилась')

    def direction(self, direction):
        print(self.name, 'машина повернула', direction)

class SportCar(Car):
    def go(self):
        print(self.name, 'спортивная машина поехала')

    def go_sport(self):
        print(self.name, 'учавствует в заезде')

    def stop(self):
        print(self.name, 'остановилась')

    def direction(self, direction):
        print(self.name, 'повернула', direction)

class TownCar(Car):
    def __init__(self, name, speed, color, is_police = 0):
        super().__init__(name, speed , color)
        self.is_police = is_police

class PoliceCar(TownCar):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        self.is_police = 1

if __name__ == '__main__':
    car_1 = Car('машина-1', 100, 'green')
    print(car_1.name, car_1.color, car_1.speed)

    car_1.go()
    car_1.stop()
    car_1.direction('left')

    sport_car = SportCar('спорт.машина-1', 200, 'red')
    sport_car.go_sport()

    town_car_1 = TownCar('раб.машина-1', 130, 'green')
    town_car_2 = TownCar(name = 'раб.машина-2', speed = 112, color = 'blue', is_police=1)

    print(town_car_1.name, town_car_1.color, town_car_1.speed, town_car_1.is_police)
    print(town_car_2.name, town_car_2.color, town_car_2.speed, town_car_2.is_police)

    police_car_1 = PoliceCar('полиц.машина-1', 120, 'white', 0) # флаг все равно поменяется на 1
    police_car_3 = PoliceCar('полиц.машина-3', 120, 'white', 1)
    print(police_car_1.name, police_car_1.color, police_car_1.speed, police_car_1.is_police)
    print(police_car_3.name, police_car_3.color, police_car_3.speed, police_car_3.is_police)

    police_car_1.go()
    police_car_1.direction('r')