mussala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_count = 0

climbers_group = int(input())

for _ in range(climbers_group):
    climbers_members = int(input())
    total_count += climbers_members

    if climbers_members <= 5:
        mussala_count += climbers_members

    elif climbers_members <= 12:
        monblan_count += climbers_members

    elif climbers_members <= 25:
        kilimanjaro_count += climbers_members

    elif climbers_members <= 40:
        k2_count += climbers_members

    else:
        everest_count += climbers_members

mussala_percent = mussala_count / total_count * 100
monblan_percent = monblan_count / total_count * 100
kilimanjaro_percent = kilimanjaro_count / total_count * 100
k2_percent = k2_count / total_count * 100
everest_percent = everest_count / total_count * 100

print(f"{mussala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
