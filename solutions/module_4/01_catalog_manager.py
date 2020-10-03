MAIN_MENU = '''
Please select a valid option:
    1) Show all movies
    2) Add/Remove movie from shopping cart
    3) Proceed to payment
    4) Generate invoice
    5) Exit

'''


SHOPPING_CART_MENU = '''
Please select a valid option:
    1) Add movie
    2) Remove movie

'''


CATALOG = [
    ['100 dias para enomorarnos', 10],
    ['Enola Holmes', 9],
    ['Yo soy beti la fea', 8],
    ['Ratched', 7],
    ['Jurassic World', 6],
    ['Father Figures', 5],
    ["The mother's killer", 4],
    ['Emoji Movie', 3],
    ['Cobra Kai', 2],
    ['Paw Patrol', 1],
]


shopping_cart_lst = []  # TODO: Issue 1


# Print menu and control program execution
def manager():
    paid = False  # TODO: Issue 2
    while True:
        opt = int(input(MAIN_MENU))
        if opt == 1:
            catalog()
        elif opt == 2:
            shopping_cart()
        elif opt == 3:
            paid = billing()
        elif opt == 4:
            invoice(paid)
        elif opt == 5:
            break
        else:
            print(f'Invalid option: {opt}')


# Print available movies at CATALOG
def catalog():
    print('--catalog--')
    for index, movie in enumerate(CATALOG):
        print(f'Index: {index}, Name: {movie[0]}, Cost: {movie[1]}')


# Select/Remove movies from shopping cart
def shopping_cart():
    print('--shopping cart--')
    opt = int(input(SHOPPING_CART_MENU))
    if opt == 1:
        index = int(input(f'Select movie index: [0-{len(CATALOG)-1}]'))
        days = int(input(f'Select number of days: '))
        movie = CATALOG[index]
        shopping_cart_lst.append([movie[0], movie[1], days])
    elif opt == 2:
        for index, item in enumerate(shopping_cart_lst):
            print(f'{index}: {item[0]}')
        index = int(input(f'Select index to remove: [0-{len(shopping_cart_lst)-1}]'))
        del shopping_cart_lst[index]
    else:
        print(f'Invalid option: {opt}')


# Display total cost for the movies, and ask user if we wants to pay or not
def billing():
    print('--billing--')
    # Shopping cart
    # [Name, Cost, Day] -> Cost * Day = total_per_movie
    # [Name, Cost, Day] -> Cost * Day = total_per_movie
    costs = [item[1] * item[2] for item in shopping_cart_lst]
    answer = input(f'Do you want to pay {sum(costs)}? (yes|no)')
    return answer == 'yes'


# Print more details about selection
def invoice(paid):
    print('--invoice--')
    if paid:
        total = 0
        print(f"| {'Movie'.center(30)} | {'Days'.center(4)} | {'Cost'.center(4)} | {'Total Cost'.center(10)}")
        for item in shopping_cart_lst:
            item_cost = item[1] * item[2]
            total += item_cost
            print(f'| {item[0]: <30} | {item[1]: <4} |{item[2]: <4} | {item_cost: <10}')
        print(f'TOTAL: {total}')
    else:
        print("You have to pay first!")


manager()
