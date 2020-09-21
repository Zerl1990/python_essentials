import random


def random_list():
    rnd_list = []
    for num in range(0, 800):
        rnd_list.append(random.randint(0, 1000))
    return rnd_list


numbers = random_list()
print(max(numbers))

