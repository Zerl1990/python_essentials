reservation_menu = '''
Select reservation type:
    0) Single
    1) Breakfast
    2) All inclusive
'''

food_menu = '''
Select food restrictions:
    0) Not Apply
    1) Vegetarian
    2) Vegan
'''


reservation_cost = 0
reservation_type = int(input(reservation_menu))
if reservation_type == 0:
    reservation_cost = 1200
elif reservation_type == 1:
    reservation_cost = 1500
elif reservation_type == 2:
    reservation_cost = 1800
else:
    cost = 0

discount = 0.0
total_nights = int(input('Select number of nights?'))
if total_nights <= 3:
    discount = 0.0
elif 3 < total_nights <= 7:
    discount = 0.15
else:
    discount = 0.30

if reservation_type == 1 or reservation_type == 2:
    food_type = int(input(food_menu))
    if food_type == 0:
        discount += 0.0
    elif food_type == 1:
        discount += 0.05
    elif food_type == 2:
        discount += 0.10


# Calculate cost without discount
cost = reservation_cost * total_nights

print('#' * 80)
print(f'Total discount: {discount}')
print(f'Cost without discount: {cost}')
print(f'Final Cost: {cost * (1.0 - discount)}')
print('#' * 80)
