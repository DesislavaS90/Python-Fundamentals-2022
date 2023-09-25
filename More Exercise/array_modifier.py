def swap_func(first, second, elements):
    elements[int(first)], elements[int(second)] = elements[int(second)], elements[int(first)]
    return elements


def multiply_func(first, second, elements):
    elements[int(first)] = elements[int(first)] * elements[int(second)]
    return elements


def modify_func(elements):

    while True:
        command = input()
        if command == 'end':
            break

        if command == 'decrease':
            for i in range(len(elements)):
                elements[i] = elements[i] - 1

        new_command = command.split(' ')
        current_command = new_command[0]

        if current_command == 'swap':
            first = new_command[1]
            second = new_command[2]
            swap_func(first, second, elements)
        elif current_command == 'multiply':
            first = new_command[1]
            second = new_command[2]
            multiply_func(first, second, elements)

    print(', '.join(map(str, elements)))


numbers = list(map(int, input().split()))
modify_func(numbers)
