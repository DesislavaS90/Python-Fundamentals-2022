def contains_func(element, keys):
    if element in keys:
        print(f'{keys} contains {element}')
    else:
        print('Substring not found!')


def flip_func(letter, start, end, keys):
    middle = keys[start:end]
    if letter == 'Upper':
        keys = keys[:start] + middle.upper() + keys[end:]
    elif letter == 'Lower':
        keys = keys[:start] + middle.lower() + keys[end:]
    print(keys)
    return keys


def slice_func(start, end, keys):
    keys = keys[:start] + keys[end:]
    print(keys)
    return keys


def main_func(key):
    while True:
        command = input().split(">>>")
        if command[0] == 'Generate':
            break
        elif command[0] == 'Contains':
            substring = command[1]
            contains_func(substring, key)

        elif command[0] == 'Flip':
            case, start_index, end_index = command[1], int(command[2]), int(command[3])
            key = flip_func(case, start_index, end_index, key)

        elif command[0] == 'Slice':
            starts_index, ends_index = int(command[1]), int(command[2])
            key = slice_func(starts_index, ends_index, key)

    print(f'Your activation key is: {key}')


activation_key = input()
main_func(activation_key)


# "Contains>>>{substring}":
# If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
# Otherwise, prints: "Substring not found!"

# "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
# Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then prints the activation key.
# All given indexes will be valid.

# "Slice>>>{startIndex}>>>{endIndex}":
# Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
# Both indices will be valid.

