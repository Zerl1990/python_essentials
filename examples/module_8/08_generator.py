class MyGenerator:
    def __init__(self, start, end):
        self.end = end
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        tmp = self.value
        self.value += 1
        return tmp


generator = MyGenerator(0, 10)
for num in generator:
    print(num)
