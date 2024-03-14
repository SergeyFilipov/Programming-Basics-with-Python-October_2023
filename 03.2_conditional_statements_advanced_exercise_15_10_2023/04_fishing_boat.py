budget = int(input())
season = input()
number_of_fishermen = int(input())

price_ship = 0
discount = 0
if season == "Spring":
    price_ship = 3000
elif season == "Summer" or season == "Autumn":
    price_ship = 4200
elif season == "Winter":
    price_ship = 2600

if number_of_fishermen <= 6:
    discount = 0.10
elif number_of_fishermen <= 11:
    discount = 0.15
elif number_of_fishermen >= 12:
    discount = 0.25

extra_discount = 0
if number_of_fishermen % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

cost_per_ship = price_ship * (1 - discount) * (1 - extra_discount)

if budget >= cost_per_ship:
    print(f"Yes! You have {budget - cost_per_ship:.2f} leva left.")
elif cost_per_ship > budget:
    print(f"Not enough money! You need {cost_per_ship - budget:.2f} leva.")
