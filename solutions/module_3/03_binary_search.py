import random


def random_list():
    rnd_list = []
    for num in range(0, 100):
        rnd_list.append(random.randint(0, 100))
    return rnd_list


numbers = random_list()

print(min(numbers))
print(max(numbers))

