class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def print(self):
        for item in self.__stack[::-1]:
            print(f'| {item: <6} |')
        print('-' * 10)


stack = Stack()

stack.push(10)
stack.push(56)
stack.push(7)
stack.print()
stack.pop()
stack.print()

