days_to_stay = int(input())
type_of_room = input()
evaluation = input()

price_room_for_one_person = 18.00
price_apartment = 25.00
price_president_apartment = 35.00

discount = 0
price_per_night = 0
if type_of_room == "room for one person":
    discount = 0
    price_per_night = price_room_for_one_person * (days_to_stay - 1) * (1 - discount)

elif type_of_room == "apartment":
    if days_to_stay < 10:
        discount = 0.30
    elif 10 <= days_to_stay <= 15:
        discount = 0.35
    elif days_to_stay > 15:
        discount = 0.50
    price_per_night = price_apartment * (days_to_stay - 1) * (1 - discount)

elif type_of_room == "president apartment":
    if days_to_stay < 10:
        discount = 0.10
    elif 10 <= days_to_stay <= 15:
        discount = 0.15
    elif days_to_stay > 15:
        discount = 0.20
    price_per_night = price_president_apartment * (days_to_stay - 1) * (1 - discount)

total_price_extra_discount = 0
if evaluation == "positive":
    extra_discount = 0.25
    total_price_extra_discount = price_per_night * (1 + extra_discount)
elif evaluation == "negative":
    extra_discount = 0.10
    total_price_extra_discount = price_per_night * (1 - extra_discount)

print(f"{total_price_extra_discount:.2f}")
