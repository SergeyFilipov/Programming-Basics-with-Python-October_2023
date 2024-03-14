budget = int(input())
seasons = input()
destination = ""
percentage_of_the_budget = 0

if budget <= 100:
    destination = "Bulgaria"
    if seasons == "summer":
        percentage_of_the_budget = 0.30
    elif seasons == "winter":
        percentage_of_the_budget = 0.70

if budget <= 1000:
    destination = "Balkans"
    if seasons == "summer":
        percentage_of_the_budget = 0.40
    elif seasons == "winter":
        percentage_of_the_budget = 0.80

if budget > 1000:
    destination = "Europe"
    percentage_of_the_budget = 0.90

if seasons == "summer" and (destination == "Bulgaria" or destination == "Balkans"):
    resting_place = "Camp"
elif seasons == "winter" and (destination == "Bulgaria" or destination == "Balkans"):
    resting_place = "Hotel"
else:
    resting_place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{resting_place} - {budget * percentage_of_the_budget:.2f}")
