from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(number):
    if number == 1 or number == 0:
        print(f'Factorial {number}: 1')
        return 1
    tmp = number * factorial(number-1)
    print(f'Factorial {number}: {tmp}')
    return tmp


factorial(5)

