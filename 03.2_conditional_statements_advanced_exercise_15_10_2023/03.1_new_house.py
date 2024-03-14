type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
total_cost = 0
discount = 0
flower_price = 0

if type_of_flowers == "Roses":
    flower_price = 5.00
    if number_of_flowers > 80:
        discount = 0.10

if type_of_flowers == "Dahlias":
    flower_price = 3.80
    if number_of_flowers > 90:
        discount = 0.15

if type_of_flowers == "Tulips":
    flower_price = 2.80
    if number_of_flowers > 80:
        discount = 0.15

if type_of_flowers == "Narcissus":
    flower_price = 3.00
    if number_of_flowers < 120:
        discount = - 0.15

if type_of_flowers == "Gladiolus":
    flower_price = 2.50
    if number_of_flowers < 80:
        discount = - 0.20

total_cost = number_of_flowers * flower_price * (1 - discount)

if budget >= total_cost:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} \
    and {budget - total_cost:.2f} leva left.")

elif total_cost > budget:
    print(f"Not enough money, you need {total_cost - budget:.2f} leva more.")
