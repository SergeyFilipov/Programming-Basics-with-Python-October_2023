judges_count = int(input())
command = input()

presentation_count = 0
total_total_score = 0

while command != "Finish":
    presentation = command
    total_score = 0
    presentation_count += 1

    for _ in range(judges_count):
        total_score += float(input())

    avr_score = total_score / judges_count
    print(f"{presentation} - {avr_score :.2f}.")
    total_total_score += total_score
    command = input()

total_avr_score = total_total_score / (presentation_count * judges_count)
print(f"Student's final assessment is {total_avr_score:.2f}.")
