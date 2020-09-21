
def scope():
    global x
    x = 10
    print(f'X: {x}')

x = 5
scope()
print(f'X: {x}')






