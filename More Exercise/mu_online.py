def potion_func(numbers, health):
    current = 0
    if health + numbers > 100:
        current = 100 - health
        health = 100
    else:
        current = numbers
        health += numbers
    print(f'You healed for {current} hp.')
    print(f'Current health: {health} hp.')
    return health


def chest_func(numbers, bitcoins):
    bitcoins += numbers
    print(f'You found {bitcoins} bitcoins.')
    return bitcoins


dungeon_rooms = input().split('|')
initial_health = 100
initial_bitcoins = 0
total_bitcoins = 0
index = 0

while index < len(dungeon_rooms):

    new_room = dungeon_rooms[index].split()
    index += 1

    room = new_room[0]
    number = new_room[1]

    if room == 'potion':
        initial_health = potion_func(int(number), initial_health)
    elif room == 'chest':
        initial_bitcoins = chest_func(int(number), initial_bitcoins)
        total_bitcoins += initial_bitcoins
        initial_bitcoins -= initial_bitcoins
    else:
        initial_health -= int(number)
        if initial_health > 0:
            print(f'You slayed {room}.')
        else:
            print(f'You died! Killed by {room}.')
            print(f'Best room: {index}')
            break
else:
    print(f'You\'ve made it!')
    print(f'Bitcoins: {total_bitcoins}')
    print(f'Health: {initial_health}')
