class Dog:
    def __init__(self, name):
        self.energy = 90
        self.name = name

    def __str__(self):
        return f"Energy {self.name}: [{'|' * self.energy:-<100}]"


def play_with_pet(pet=None):
    print(pet)


dog = Dog('Bacon')
play_with_pet()