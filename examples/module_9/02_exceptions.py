
try:
    print(10 / 0)
except (ValueError, ZeroDivisionError):
    print('Invalid Operations')
except:
    print('Unexpected error')
