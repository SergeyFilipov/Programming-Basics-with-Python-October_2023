actor_name = input()
actor_academy_points = float(input())
count_of_evaluators = int(input())
total_points = actor_academy_points

for _ in range(count_of_evaluators):
    evaluators_name = input()
    evaluators_points = float(input())
    actor_points = len(evaluators_name) * evaluators_points / 2
    total_points += actor_points
    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")
