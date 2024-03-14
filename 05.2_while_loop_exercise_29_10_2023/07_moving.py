width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
space_left = total_space

command = input()
while command != "Done":
    current_boxes = int(command)
    space_left -= current_boxes
    if space_left <= 0:
        break
    command = input()

if command == "Done":
    print(f"{space_left} Cubic meters left.")
else:
    space_needed = -space_left
    print(f"No more free space! You need {space_needed} Cubic meters more.")
