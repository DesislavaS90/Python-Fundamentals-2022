inventory = input().split(', ')

while True:

    command = input()

    if command == 'Craft!':
        break

    new = command.split(' - ')

    current_command = new[0]

    if current_command == 'Collect':
        word = new[1]
        if word not in inventory:
            inventory.append(word)

    elif current_command == 'Drop':
        word1 = new[1]
        if word1 in inventory:
            inventory.remove(word1)

    elif current_command == 'Combine Items':
        words = new[1].split(':')
        old = words[0]
        news = words[1]
        if old in inventory:
            index = inventory.index(old)
            inventory.insert(index + 1, news)

    elif current_command == 'Renew':
        word2 = new[1]
        if word2 in inventory:
            inventory.remove(word2)
            inventory.append(word2)

print(', '.join(inventory))


