class NoCreditException(Exception):
    pass


try:
    raise NoCreditException('No credit available')
except NoCreditException as exception:
    print(f'Catch exception: {exception}')

