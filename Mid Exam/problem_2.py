coffee_list = input().split()
count_of_commands = int(input())

for command in range(1, count_of_commands + 1):
    commands = input().split()

    if commands[0] == 'Include':
        coffee_list.append(commands[1])

    elif commands[0] == 'Remove':
        if commands[1] == 'first':
            number = int(commands[2])
            if number <= len(coffee_list):
                counter = 0
                for i in range(len(coffee_list)):
                    coffee_list.pop(0)
                    counter += 1
                    if counter == number:
                        break

        elif commands[1] == 'last':
            numbers = int(commands[2])
            if numbers <= len(coffee_list):
                counter = 0
                for i in range(len(coffee_list)):
                    coffee_list.pop()
                    counter += 1
                    if counter == numbers:
                        break

    elif commands[0] == 'Prefer':
        first_index = int(commands[1])
        second_index = int(commands[2])
        if len(coffee_list) > first_index and len(coffee_list) > second_index:
            coffee_list[first_index], coffee_list[second_index] = coffee_list[second_index], coffee_list[first_index]

    elif commands[0] == 'Reverse':
        coffee_list = coffee_list[::-1]

print("Coffees:")
print(' '.join(coffee_list))