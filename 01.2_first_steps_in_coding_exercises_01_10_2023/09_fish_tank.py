length = int(input())
width = int(input())
height = int(input())
percent_not_empty = float(input()) / 100

fish_tank_volume = length * width * height
volume_in_liters = fish_tank_volume / 1000

water_needed_liters = volume_in_liters * (1 - percent_not_empty)

print(water_needed_liters)
