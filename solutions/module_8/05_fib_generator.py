
# fib(n) = fib(n-1) + fib(n-2)

def fib_r(num):
    if num < 2:
        return 1
    return fib(num-1) + fib(num-2)


def fib(end):
    # Fib0 - 1
    # Fib1 - 1
    # Fib2 - 2
    # Fib3 - 3
    # Fib4 - 5
    # Fib5 - 8
    # Fib6 - 13
    results = [1, 1, 2]  # 3
    for index in range(1, end+1):
        if index <= 2:
            yield results[index]
        else:
            results.append(results[index-1] + results[index-2])
            yield results[index]


for num in fib(10):
    print(num)
