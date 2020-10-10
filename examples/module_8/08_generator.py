class MyIterator:
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


iterator = MyIterator(15, 200)
for num in iterator:
    print(num)

print(sum(MyIterator(15, 200)))
