"""OOP Exercise."""
import random
from string import ascii_letters as letters


class Vehicle:
    """Vehicle"""
    def __init__(self, name: str, max_speed: float, milage: float, capacity: int):
        self.__name = name
        self.__max_speed = max_speed
        self.__milage = milage
        self.__capacity = capacity

    def get_name(self) -> str:
        """Get name"""
        return self.__name

    def get_max_speed(self) -> str:
        """Get max speed"""
        return self.__max_speed

    def get_milage(self) -> str:
        """Get Milage"""
        return self.__milage

    def get_capacity(self) -> str:
        """Get capacity"""
        return self.__capacity

    def set_capacity(self, value: int):
        """Set Capacity"""
        if value and type(value) == int and 0 <= value <= 5:
            self.__capacity = value
        else:
            raise ValueError(f'Invalid capacity {value}, it should be between 0 and 5')

    def __str__(self):
        return f'Name: {self.__name}, Max Speed: {self.__max_speed}, Milage: {self.__milage}, Capacity: {self.__capacity}'


class Person:
    """Person."""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        """Get name"""
        return self.__name

    def get_age(self):
        """Get age."""
        return self.__age

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}'


class Bus(Vehicle):
    """Bus."""
    def __init__(self, name, milage):
        super().__init__(name, milage, 80, 50)
        self.__passenger = []

    def pick(self, person):
        """Pick"""
        if len(self.__passenger) > 50:
            raise RuntimeError('Max capacity exceeded')
        print('Pick')
        self.__passenger.append(person)
        print(self)

    def drop(self):
        """Drop person"""
        print('Drop')
        self.__passenger.pop()
        print(self)

    def __str__(self):
        base = super().__str__()
        return base + f', Passengers: {len(self.__passenger)}'


bus = Bus('School Bus', 0)
print(bus)

for index in range(0, 10000):
    action = random.randint(0, 1)
    if action == 0:
        bus.drop()
    else:
        t_name = ''.join([random.choice(letters) for _ in range(8)])
        t_age = random.randint(5, 100)
        t_person = Person(t_name, t_age)
        bus.pick(t_person)




