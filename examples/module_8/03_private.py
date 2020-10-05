
class Dog:
    def __init__(self, color):
        self.color = color
        self.__energy = 100

    def play(self):
        self.__energy -= 5

    def eat(self):
        self.__energy += 5


hasattr(Dog, 'sleep')

