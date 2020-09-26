flavor_menu = '''
Please select a flavor:
    0) Lemon
    1) Vanilla
    2) Chocolate

'''

topping_menu = '''
Please select topping:
    0) No topping
    1) Oreo
    2) Kitkat
    3) Brownie

'''

flavor = int(input(flavor_menu))
topping = int(input(topping_menu))
cost = 0

#  Flavor
if flavor == 0:
    cost = 23
elif flavor == 1:
    cost = 22
elif flavor == 2:
    cost = 26
else:
    cost = 0

# Topping
if topping == 0:
    cost += 0
elif topping == 1:
    cost += 15
elif topping == 2:
    cost += 22.5
elif topping == 3:
    cost += 13.3
else:
    cost += 0

if cost == 0:
    print('Invalid selection, cost is 0!')
else:
    print(f'Cost: {cost}')
