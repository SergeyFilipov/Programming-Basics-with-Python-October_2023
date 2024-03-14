month = input()
number_of_nights = int(input())
price_studio = 0
price_apartment = 0
discount_studio = 0
discount_apartment = 0

if month == "May" or month == "October":
    price_studio = 50.00
    price_apartment = 65.00
    if 7 < number_of_nights <= 14:
        discount_studio = 0.05
        discount_apartment = 0
    elif number_of_nights > 14:
        discount_studio = 0.30
        discount_apartment = 0.10

elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if number_of_nights > 14:
        discount_studio = 0.20
        discount_apartment = 0.10

elif month == "July" or month == "August":
    price_studio = 76.00
    price_apartment = 77.00
    if number_of_nights > 14:
        discount_apartment = 0.10

total_studio_price = number_of_nights * price_studio * (1 - discount_studio)
total_apartment_price = number_of_nights * price_apartment * (1 - discount_apartment)

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")
