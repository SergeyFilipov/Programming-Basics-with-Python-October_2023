count_of_numbers = int(input())
even_sum = 0
odd_sum = 0

for numbers in range(count_of_numbers):
    current_of_numbers = int(input())
    if numbers % 2 == 0:
        even_sum += current_of_numbers
    else:
        odd_sum += current_of_numbers

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {difference}")
