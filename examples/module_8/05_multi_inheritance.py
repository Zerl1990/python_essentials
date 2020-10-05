class SuperA:
    def __init__(self):
        self.super_a = 10

    def function_a(self):
        return 'function a'


class SuperB:
    def __init__(self):
        self.super_b = 15

    def function_b(self):
        return 'function b'


class Child(SuperA, SuperB):
    def __init__(self):
        super(SuperA)
        super(SuperB)
