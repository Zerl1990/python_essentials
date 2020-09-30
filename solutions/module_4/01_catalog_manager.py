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


SHOPPING_CART = []


# Print menu and control program execution
def manager():
    while True:
        opt = int(input(MAIN_MENU))
        paid = False
        if opt == 1:
            catalog()
        elif opt == 2:
            shopping_cart()
        elif opt == 3:
            billing()
        elif opt == 4:
            invoice(paid)
        elif opt == 5:
            break
        else:
            print(f'Invalid option: {opt}')


# Print available movies at CATALOG
def catalog():
    print('catalog')


# Select/Remove movies from shopping cart
def shopping_cart():
    print('shopping cart')
    opt = int(input(SHOPPING_CART_MENU))
    if opt == 1:
        # Add movie to SHOPPING_CART
        pass
    elif opt == 2:
        # Remove movie by index from SHOPPING_CART
        pass
    else:
        print(f'Invalid option: {opt}')


# Display total cost for the movies, and ask user if we wants to pay or not
def billing():
    print('billing')
    paid = False
    return paid


# Print more details about selection
def invoice(paid):
    print('billing')


manager()
