import random


def random_list():
    rnd_list = []
    for num in range(0, 100):
        rnd_list.append(random.randint(0, 100))
    return rnd_list


numbers = random_list()


target = int(input('Provide number to search: '))
numbers.sort()

low = 0
high = len(numbers) - 1
mid = 0
found = False

print('')
while low <= high:
    mid = (high + low) // 2
    print(f"\t{low}{'-' * 10}{mid:->2}[{numbers[mid]: >2}]{'-' * 10}{high}")

    # Number is in right half
    if numbers[mid] < target:
        low = mid + 1

    # Number is in left half
    elif numbers[mid] > target:
        high = mid - 1

    # If x is smaller, ignore right half
    else:
        found = True
        break

print(f'Found: {found}')
print(numbers)

