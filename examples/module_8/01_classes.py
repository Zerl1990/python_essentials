class Car:
    class_variable = 'class variable'

    def __init__(self, color):
        self.color = color
        self.position = 0

    def move(self, distance):
        self.position += distance

    def get_class_variable(self):
        return self.class_variable

    @classmethod
    def modify_class_variable(cls):
        cls.class_variable = f'Modified by {cls.__name__}'


car_1 = Car(color='red')
car_2 = Car(color='blue')
print(car_1.__dict__)
print(car_2.__dict__)
print(car_1.get_class_variable())
car_1.modify_class_variable()
print(car_2.get_class_variable())


