import random

print((
    "+=========================================+\n"
    "| Guess my number!                        |\n"
    "| Please, select a numbers between [0-100]|\n"
    "| Let's start you have 10 opportunities   |\n"
    "+=========================================+\n"
))

my_number = random.randint(0, 100)
opportunities = 0
max_opportunities = 10
guess = -1
win = False

while not win and opportunities < max_opportunities:
    guess = int(input('What is the number?: '))
    win = (my_number == guess)
    opportunities += 1
    if my_number < guess:
        print(f'[---] My number is less than {guess}')
    elif my_number > guess:
        print(f'[+++] My number is greater than {guess}')
    else:
        print('You found my number!')

if win:
    print(f'It only took {opportunities} opportunities, you have won!!!')
else:
    print("Better luck next time")



