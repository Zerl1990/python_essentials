
try:
    print(10 / 0)
except (ValueError, ZeroDivisionError) as exception:
    print(f'Invalid Operations: {exception}')
finally:
    print('Done!')
