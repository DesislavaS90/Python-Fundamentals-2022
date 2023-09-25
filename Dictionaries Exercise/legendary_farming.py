dictionary = {'shards': 0, 'fragments': 0, 'motes': 0}

while True:
    items = input().split()

    for index in range(0, len(items), 2):
        key = items[index + 1].lower()
        value = int(items[index])

        if key not in dictionary:
            dictionary[key] = 0
        dictionary[key] += value

        if dictionary['shards'] >= 250 or dictionary['fragments'] >= 250 or dictionary['fragments'] >= 250:
            break

    if dictionary['shards'] >= 250:
        dictionary['shards'] -= 250
        print('Shadowmourne obtained!')
        break
    elif dictionary['fragments'] >= 250:
        dictionary['fragments'] -= 250
        print('Valanyr obtained!')
        break
    elif dictionary['motes'] >= 250:
        dictionary['motes'] -= 250
        print('Dragonwrath obtained!')
        break

for material, quantity in dictionary.items():
    print(f'{material}: {quantity}')