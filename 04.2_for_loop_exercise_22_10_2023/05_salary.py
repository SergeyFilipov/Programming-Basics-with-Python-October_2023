opened_tabs_count = int(input())
salary = float(input())

for _ in range(opened_tabs_count):
    current_website = input()

    if current_website == "Facebook":
        salary -= 150
    elif current_website == "Instagram":
        salary -= 100
    elif current_website == "Reddit":
        salary -= 504

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(int(salary))
