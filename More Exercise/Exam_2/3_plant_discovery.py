import re
number = int(input())

my_dict = {}
ratings = {}

for _ in range(number):
    plant = input().split('<->')
    if plant[0] not in my_dict:
        my_dict[plant[0]] = int(plant[1])
        ratings[plant[0]] = []
    my_dict[plant[0]] = int(plant[1])

while True:

    command = input()
    if command == 'Exhibition':
        break

    current_command = re.split(': | - ', command)

    if current_command[0] == 'Rate':
        plant, rating = current_command[1], int(current_command[2])
        if plant in ratings:
            ratings[plant] += [rating]
        else:
            print('error')
    elif current_command[0] == 'Update':
        plant, new_rarity = current_command[1], int(current_command[2])
        if plant in my_dict:
            my_dict[plant] = new_rarity
        else:
            print('error')
    elif current_command[0] == 'Reset':
        plant = current_command[1]
        if plant in ratings:
            ratings[plant] = []
        else:
            print('error')

print('Plants for the exhibition:')

for key, value in my_dict.items():
    if not ratings[key]:
        average = 0
    else:
        average = sum(ratings[key]) / len(ratings[key])
    print(f'- {key}; Rarity: {value}; Rating: {average:.2f}')

# After that, until you receive the command "Exhibition", you will be given some of these commands:
# "Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# "Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# "Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"

# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition: - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating} …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.
