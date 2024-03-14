seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

total_second = seconds_first + seconds_second + seconds_third

minutes = total_second // 60
seconds = total_second % 60

print(f"{minutes}:{seconds:02d}")
