class MyIterator:
    def __init__(self, start, end, mod):
        self.end = end
        self.value = start
        self.mod = mod

    def __iter__(self):
        return self

    def __next__(self):
        # Search next number
        while self.value % self.mod != 0:
            self.value += 1""

        # Store number
        tmp = self.value

        # Move
        self.value += 1

        # Verify range
        if tmp >= self.end:
            raise StopIteration
        else:
            return tmp


iterator = MyIterator(2, 100000, 3)
for num in iterator:
    print(num)
