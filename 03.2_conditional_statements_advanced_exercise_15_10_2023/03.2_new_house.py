type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
total_price = 0

if type_of_flowers == "Roses":
    if number_of_flowers <= 80:
        total_price = number_of_flowers * 5
    elif number_of_flowers > 80:
        total_price = number_of_flowers * (5 * (1 - 0.10))

if type_of_flowers == "Dahlias":
    if number_of_flowers <= 90:
        total_price = number_of_flowers * 3.80
    elif number_of_flowers > 90:
        total_price = number_of_flowers * (3.80 * (1 - 0.15))

if type_of_flowers == "Tulips":
    if number_of_flowers <= 80:
        total_price = number_of_flowers * 2.80
    elif number_of_flowers > 80:
        total_price = number_of_flowers * (2.80 * (1 - 0.15))

if type_of_flowers == "Narcissus":
    if number_of_flowers >= 120:
        total_price = number_of_flowers * 3.00
    elif number_of_flowers < 120:
        total_price = number_of_flowers * (3.00 * (1 + 0.15))

if type_of_flowers == "Gladiolus":
    if number_of_flowers >= 80:
        total_price = number_of_flowers * 2.50
    elif number_of_flowers < 80:
        total_price = number_of_flowers * (2.50 * (1 + 0.20))

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and \
{budget - total_price:.2f} leva left.")

elif total_price > budget:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
