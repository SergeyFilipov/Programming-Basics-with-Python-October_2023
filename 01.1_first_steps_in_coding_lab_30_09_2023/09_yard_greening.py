total_price_per_square_meter = float(input()) * 7.61
discount = 0.18
final_price = total_price_per_square_meter - (total_price_per_square_meter * discount)
print(f"The final price is: {final_price} lv.")

the_discount = total_price_per_square_meter * discount

print(f"The discount is: {the_discount} lv.")
