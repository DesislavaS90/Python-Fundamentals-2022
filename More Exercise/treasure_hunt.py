loot = input().split('|')

stolen = []

while True:
    command = input()

    if command == 'Yohoho!':
        break
    current_command = command.split()

    if current_command[0] == 'Loot':
        for word in current_command:
            if word not in loot and word != current_command[0]:
                loot.insert(0, word)
    elif current_command[0] == 'Drop':
        item = int(current_command[1])
        if item <= len(loot):
            x = loot.pop(item)
            loot.append(x)
    elif current_command[0] == 'Steal':
        number = int(current_command[1])
        if number <= len(loot):
            loot = loot[:-number]
        print(', '.join(stolen))


if len(loot) == 0:
    print('Failed treasure hunt.')
sum_counter = 0
for word in loot:
    sum_counter += len(word)
else:
    average_gain = sum_counter / len(loot)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')
