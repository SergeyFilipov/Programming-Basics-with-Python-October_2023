Peter_budget = float(input())
number_of_video_cards = int(input())
number_of_procesors = int(input())
number_frame_of_mind = int(input())

price_video_cards = number_of_video_cards * 250
price_procesors = number_of_procesors * (price_video_cards * 0.35)
price_frame_of_mind = number_frame_of_mind * (price_video_cards * 0.10)
total_price = price_procesors + price_frame_of_mind + price_video_cards

if number_of_video_cards > number_of_procesors:
    final_price = total_price * 0.85
else:
    final_price = total_price

if final_price <= Peter_budget:
    print(f"You have {Peter_budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price - Peter_budget:.2f} leva more!")
