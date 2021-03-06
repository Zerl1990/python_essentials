class Pet:
    def __init__(self, name, **kwargs):
        self.name = name
        self.age = kwargs.get('age', 0)
        self.height = int(kwargs.get('height', 0))
        self.weight = int(kwargs.get('weight', 0))
        self.__species = int(kwargs.get('species', 0))
        self.__energy = int(kwargs.get('energy', 0))
        self.__species_factor = self.age + self.height + self.weight + self.__species

    def play(self, time_sec):
        self.__energy -= time_sec * (self.__species_factor / 100)

    def run(self, distance_m):
        self.__energy -= distance_m * (self.__species_factor / 95)

    def sleep(self, time_sec):
        self.__energy += time_sec * (self.__species_factor / 100)

    def eat(self, qty):
        self.__energy += qty * (self.__species_factor / 95)

    def get_energy(self):
        return self.__energy

    def __str__(self):
        return f"Energy {self.__species} {self.name}: [{'|' * int(self.__energy):-<100}]"


class Dog(Pet):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age=age, height=height, weight=weight, species=2, energy=100)

    def bark(self):
        print(f'[{self.name}] - BARK!')


class Cat(Pet):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age=age, height=height, weight=weight, species=4, energy=80)

    def meow(self):
        print(f'[{self.name}] - MEOW!')


class Kid:
    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        self.__pets = args
        self.__kid_factor = 6 * (20 - self.age)

    def play_with_pets(self):
        for pet in self.__pets:
            if pet.get_energy() > 0:
                print(f'{self.name} playing with {pet.name}')
                print(pet)
                pet.play(self.__kid_factor)
                print(pet)
            if isinstance(pet, Dog):
                pet.bark()
            if isinstance(pet, Cat):
                pet.meow()

    def feed_pets(self):
        for pet in self.__pets:
            if pet.get_energy() != 100:
                print(f'{self.name} feed {pet.name}')
                print(pet)
                pet.eat(self.__kid_factor)
                print(pet)

    def __str__(self):
        return f"{self.name}, total pets: {len(self.__pets)}"


# Main logic
dog = Dog('Bacon', 10, 40, 10)
cat = Cat('Cat', 4, 20, 6)
kid = Kid('Kid', 5, dog, cat)
kid.play_with_pets()
kid.feed_pets()
