
def multiple(num_a, num_b):
    if type(num_a) != int or type(num_b) != num_b:
        raise ValueError
    return num_a * num_b


try:
    multiple("2432", 25)
except ValueError:
    print('Invalid Error')

