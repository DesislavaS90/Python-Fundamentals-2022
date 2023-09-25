energy = int(input())

won_battle = 0
end_energy = False

while True:
    command = input()

    if command == 'End of battle':
        break

    distance = int(command)

    if energy < distance:
        end_energy = True
        break
    if distance <= energy:
        energy -= distance
        won_battle += 1
    if won_battle % 3 == 0:
        energy += won_battle


if end_energy:
    print(f'Not enough energy! Game ends with {won_battle} won battles and {energy} energy')

else:
    print(f'Won battles: {won_battle}. Energy left: {energy}')
