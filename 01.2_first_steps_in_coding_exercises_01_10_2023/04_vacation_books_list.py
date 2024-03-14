total_peges = int(input())
peges_per_hour = int(input())
days = int(input())

total_hours_per_needed = total_peges // peges_per_hour

hours_per_day_needed = total_hours_per_needed / days

print(int(hours_per_day_needed))
