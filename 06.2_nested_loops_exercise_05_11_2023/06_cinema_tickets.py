student_tickets = 0
standard_tickets = 0
kids_tickets = 0

command1 = input()
while command1 != "Finish":
    movie_name = command1
    total_seats = int(input())

    ticket_bought = 0
    command2 = input()
    while command2 != "End":
        ticket_bought += 1

        if command2 == "student":
            student_tickets += 1
        elif command2 == "standard":
            standard_tickets += 1
        elif command2 == "kid":
            kids_tickets += 1

        if ticket_bought == total_seats:
            break

        command2 = input()

    percent_full = ticket_bought / total_seats * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    command1 = input()

total_tickets = student_tickets + standard_tickets + kids_tickets
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")
