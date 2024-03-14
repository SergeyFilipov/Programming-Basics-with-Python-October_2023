import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1_m = float(input())

required_distance_in_second = distance_in_meters * time_in_seconds_for_1_m
slowdown = math.floor(distance_in_meters / 15) * 12.5
Total_time_Ivan = required_distance_in_second + slowdown

if record_in_seconds <= Total_time_Ivan:
    print(f"No, he failed! He was {Total_time_Ivan - record_in_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {Total_time_Ivan:.2f} seconds.")
