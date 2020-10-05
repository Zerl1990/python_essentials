class Pet:
    def __init__(self, name, species):
        self.energy = 90
        self.name = name
        self.species = 0

    def __str__(self):
        return f"Energy {self.species} {self.name}: [{'|' * self.energy:-<100}]"


class Kid:
    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        self.__pets = []

    def __str__(self):
        return f"{self.name}, total pets: {len(self.__pets)}"

