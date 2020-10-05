import time


class Cellphone:
    def __init__(self, processor):
        self.processor = processor

    def sum(self, num_a, num_b):
        self.processor.compute('+', num_a, num_b)


class Processor:
    def compute(self, operator, num_a, num_b):
        if operator == '+':
            self.sum(num_a, num_b)
        elif operator == '-':
            self.subs(num_a, num_b)
        else:
            raise ValueError('Invalid operator!')

    def sum(self, num_a, num_b):
        raise NotImplemented

    def subs(self, num_a, num_b):
        raise NotImplemented


class ProcessorA(Processor):
    def sum(self, num_a, num_b):
        time.sleep(1)
        return num_a + num_b

    def subs(self, num_a, num_b):
        time.sleep(1)
        return num_a - num_b


class ProcessorB(Processor):
    def sum(self, num_a, num_b):
        time.sleep(3)
        return num_a + num_b

    def subs(self, num_a, num_b):
        time.sleep(3)
        return num_a - num_b


processor = ProcessorB()
cellphone = Cellphone(processor)
cellphone.sum(5, 4)
