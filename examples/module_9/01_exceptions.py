
try:
    print(10 / 0)
except ValueError:
    print('Value error')
except ZeroDivisionError:
    print('Zero division error')
except:
    print('Unexpected error')


