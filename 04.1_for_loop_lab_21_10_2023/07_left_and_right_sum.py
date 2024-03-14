count_of_numbers = int(input())
left_sum = 0
right_sum = 0

for numbers in range(2 * count_of_numbers):
    current_of_numbers = int(input())
    if numbers < count_of_numbers:
        left_sum += current_of_numbers
    else:
        right_sum += current_of_numbers
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
