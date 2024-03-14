concurrent_hour = int(input())
concurrent_minute = int(input())

concurrent_time_in_minutes = (concurrent_hour * 60) + concurrent_minute + 15
current_time_as_hour = concurrent_time_in_minutes // 60
if current_time_as_hour == 24:
    current_time_as_hour = 0

current_time_as_minutes = concurrent_time_in_minutes % 60
print(f"{current_time_as_hour}:{current_time_as_minutes:02d}")
