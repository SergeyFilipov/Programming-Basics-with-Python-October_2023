chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
vegetarian_menu = int(input()) * 8.15
dessert = (chicken_menu + fish_menu + vegetarian_menu) * (1 - 0.8)
the_cost_of_delivery = 2.50

total_cost = chicken_menu + fish_menu + vegetarian_menu \
             + dessert + the_cost_of_delivery

print(total_cost)
