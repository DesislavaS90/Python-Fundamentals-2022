my_cities = {}
while True:
    command = input().split('||')

    if command[0] == 'Sail':
        break

    city, population, gold = command[0], int(command[1]), int(command[2])

    if city not in my_cities:
        my_cities[city] = [population, gold]
    else:
        my_cities[city][0] += population
        my_cities[city][1] += gold

while True:
    current_command = input().split('=>')

    if current_command[0] == 'End':
        break

    elif current_command[0] == 'Plunder':
        town, people, gold = current_command[1], int(current_command[2]), int(current_command[3])
        my_cities[town][0] -= people
        my_cities[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if my_cities[town][0] == 0 or my_cities[town][1] == 0:
            del my_cities[town]
            print(f'{town} has been wiped off the map!')

    elif current_command[0] == 'Prosper':
        town, gold = current_command[1], int(current_command[2])

        if gold < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            my_cities[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {my_cities[town][1]} gold.')

if my_cities:
    print(f'Ahoy, Captain! There are {len(my_cities)} wealthy settlements to go to:')
    for key, value in my_cities.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')



# "Plunder=>{town}=>{people}=>{gold}"
# You have successfully attacked and plundered the town, killing the given number of people and stealing the respective amount of gold.
# For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# If any of those two values (population or gold) reaches zero, the town is disbanded.
# You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off the map!"
# There will be no case of receiving more people or gold than there is in the city.

# "Prosper=>{town}=>{gold}"
# There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added cannot be a negative number!" and ignore the command.
# If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the following message:
