packet_of_chemicals = int(input()) * 5.80
marker_pack = int(input()) * 7.20
preparation = int(input()) * 1.20
percentage_reduction = int(input()) / 100

price_for_all_materials = (packet_of_chemicals + marker_pack + preparation)
discounted_price = price_for_all_materials - (price_for_all_materials * percentage_reduction)
print(discounted_price)
