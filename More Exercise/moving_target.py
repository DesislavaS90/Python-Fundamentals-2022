def shoot_func(index, number, elements):
    if 0 <= index <= len(elements):
        if elements[index] - number <= 0:
            elements.pop(index)
        else:
            elements[index] = elements[index] - number
    return elements


def add_func(index, number, elements):
    if 0 <= index < len(elements):
        elements.insert(index, number)
    else:
        print('Invalid placement!')
    return elements


def strike_func(index, number, elements):
    if index - number >= 0 and index + number < len(elements):
        start = index - number
        final = index + number
        elements = [elements[i] for i in range(len(elements)) if i < start or i > final]
    else:
        print('Strike missed!')
    return elements


def commands_func(elements):

    while True:
        command = input()
        if command == 'End':
            break
        target, index, number = command.split()

        if target == 'Shoot':
            elements = shoot_func(int(index), int(number), elements)
        elif target == 'Add':
            elements = add_func(int(index), int(number), elements)
        elif target == 'Strike':
            elements = strike_func(int(index), int(number), elements)
    print('|'.join(map(str, elements)))


targets = list(map(int, input().split()))
commands_func(targets)