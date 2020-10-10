class MyIterator:
    def __init__(self, start, end):
        self.end = end
        self.value = start
        if self.value % 2 != 0:
            self.value += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        tmp = self.value
        self.value += 2
        return tmp


iterator = MyIterator(15, 200)
for num in iterator:
    print(num)
