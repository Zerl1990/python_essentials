my_set = set()
print(type(my_set))

set_a = {1, 2, 3, 4}

set_b = {1, 2, 8, 9, 10}

print(f'A: {set_a}')
print(f'B: {set_b}')

print(f'A union B: {set_a.symmetric_difference(set_b)}')
print(f'A intersection B: {set_a.intersection(set_b)}')
print(f'A difference B: {set_a.difference(set_b)}')
print(f'A symmetric difference B: {set_a.symmetric_difference(set_b)}')

