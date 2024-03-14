budget = float(input())
people_count = int(input())
clothing_for_one_people = float(input())

decor = budget * 0.10

if people_count > 150:
    clothing_for_one_people = clothing_for_one_people * (1 - 0.10)

money_needed = decor + people_count * clothing_for_one_people

if money_needed > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {money_needed - budget:.2f} leva more.")
    print(f"Action!")
    print(f"Wingard starts filming with {budget - money_needed:.2f} leva left.")
