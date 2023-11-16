class Car:

    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price

    def go(self):
        print('Дана машина:')
        print(f'Модель: {self.name}')
        print(f'Максимальная скорость: {self.speed}')
        print(f'Стоимость: {self.price}')

my_car = Car('BMW M4', '300km/h', '300000$')
my_car.go()