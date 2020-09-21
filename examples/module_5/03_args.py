
def print_names(tabs, *args, end=None):
    for name in args:
        print('\t' * tabs + f'{name}{end}')


print_names(5, 'Luis', 'Ana', 'Rogelio', 'Felipe', end='!')



