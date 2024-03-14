projection_type = input()
number_of_rows = int(input())
number_of_columns = int(input())
total_ticket_revenue = 0

if projection_type == "Premiere":
    total_ticket_revenue = number_of_columns * number_of_rows * 12.00

elif projection_type == "Normal":
    total_ticket_revenue = number_of_columns * number_of_rows * 7.50

elif projection_type == "Discount":
    total_ticket_revenue = number_of_columns * number_of_rows * 5.00

print(f"{total_ticket_revenue:.2f} leva")
