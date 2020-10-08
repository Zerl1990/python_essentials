class Dog:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__energy = 100

    def play(self, time_sec):
        print(f'{self.name} - play')
        self.__energy = self.__energy - time_sec * ((self.age + self.height + self.weight)/100)

    def run(self, distance_m):
        print(f'{self.name} - run')
        self.__energy -= distance_m * ((self.age + self.height + self.weight)/95)

    def sleep(self, time_sec):
        print(f'{self.name} - sleep')
        self.__energy += time_sec * ((self.age + self.height + self.weight)/100)

    def eat(self, qty):
        print(f'{self.name} - eat')
        self.__energy += qty * ((self.age + self.height + self.weight)/95)

    def __str__(self):
        return f"Energy {self.name}: [{'|' * int(self.__energy):-<100}]"


def play_with_pet(pet: Dog):
    pet.play(10)
    print(pet)
    pet.run(5)
    print(pet)
    pet.eat(23)
    print(pet)


dog_1 = Dog('Bacon', 3, 34, 7)
dog_2 = Dog('Pet2', 1, 23, 5)
play_with_pet(dog_1)
play_with_pet(dog_2)
