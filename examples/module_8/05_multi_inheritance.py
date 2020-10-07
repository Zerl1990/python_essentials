class SuperA:
    def __init__(self):
        print('SuperA Constructor')
        super().__init__()
        self.super_a = 10

    def function_a(self):
        return 'function a'


class SuperB:
    def __init__(self):
        print('SuperB Constructor')
        super().__init__()
        self.super_b = 15

    def function_b(self):
        return 'function b'


class Child(SuperA, SuperB):
    def __init__(self):
        print('Child Constructor')
        super().__init__()


print(SuperA.__mro__)  # Print method resolution order
print(SuperB.__mro__)  # Print method resolution order
print(Child.__mro__)  # Print method resolution order
child = Child()
