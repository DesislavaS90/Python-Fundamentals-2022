needed_experience = float(input())
count_of_battles = int(input())

counter = 0
battle_counter = 0

for battle in range(1, count_of_battles + 1):
    experience = float(input())
    counter += experience
    battle_counter += 1

    if battle % 15 == 0:
        counter += experience * 0.05
    elif battle % 3 == 0:
        counter += experience * 0.15
    elif battle % 5 == 0:
        counter += experience - (experience * 1.1)
    if counter >= needed_experience:
        break
if counter >= needed_experience:
    print(f'Player successfully collected his needed experience for {battle_counter} battles.')
else:
    diff = needed_experience - counter
    print(f'Player was not able to collect the needed experience, {diff:.2f} more needed.')

