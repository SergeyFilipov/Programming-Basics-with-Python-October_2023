city = input()
sales_volume = float(input())
trade_commission = 0

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.07
    elif 1000 < sales_volume <= 10_000:
        trade_commission = sales_volume * 0.08
    elif 10_000 < sales_volume:
        trade_commission = sales_volume * 0.12

if city == "Varna":
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.075
    elif 1000 < sales_volume <= 10_000:
        trade_commission = sales_volume * 0.10
    elif 10_000 < sales_volume:
        trade_commission = sales_volume * 0.13

if city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        trade_commission = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        trade_commission = sales_volume * 0.08
    elif 1000 < sales_volume <= 10_000:
        trade_commission = sales_volume * 0.12
    elif 10_000 < sales_volume:
        trade_commission = sales_volume * 0.145

if trade_commission == 0:
    print("error")
else:
    print(f"{trade_commission:.2f}")
