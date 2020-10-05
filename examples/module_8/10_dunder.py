class Car:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __str__(self):
        return f'Car {self.color}'

    def __len__(self):
        return self.size


car = Car('red', 10)
print(len(car))


