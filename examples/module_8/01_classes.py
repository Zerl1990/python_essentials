class Car:
    class_variable = 'class variable'
    total_instance = 0

    def __init__(self, color):
        self.color = color
        self.position = 0
        Car.total_instance += 1

    def move(self, distance):
        self.position += distance

    def get_class_variable(self):
        return self.class_variable

    def get_total_instances(self):
        return self.total_instance

    @classmethod
    def modify_class_variable(cls):
        cls.class_variable = f'Modified by {cls.__name__}'


car_1 = Car(color='red')
car_2 = Car(color='blue')
car_3 = Car(color='yellow')
print(car_1.__dict__)
print(car_2.__dict__)
print(car_1.get_class_variable())
car_1.modify_class_variable()
print(car_2.get_class_variable())
print(car_3.get_class_variable())

print(car_3.get_total_instances())


