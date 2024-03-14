hour_of_the_exam = int(input())
minute_of_the_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

total_minute_exam = hour_of_the_exam * 60 + minute_of_the_exam
total_minute_arrival = hour_of_arrival * 60 + minute_of_arrival

diff = total_minute_arrival - total_minute_exam

if diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hh = diff // 60
        mm = diff % 60
        print(f"{hh}:{mm:02d} hours after the start")

elif diff >= -30:
    print("On time")
    if not diff == 0:
        print(f"{abs(diff)} minutes before the start")
else:
    print("Early")
    if diff > -60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hh = abs(diff) // 60
        mm = abs(diff) % 60
        print(f"{hh}:{mm:02d} hours before the start")
