elements = input().upper()

last_symbol = ''
filtered = ''
counter = 0
number = ''

for index in range(len(elements)):
    if not elements[index].isdigit():
        last_symbol += elements[index]
        if elements[index] not in filtered:
            counter += 1

    elif elements[index].isdigit():
        number += elements[index]
        if index != len(elements) - 1:
            if elements[index + 1].isdigit():
                number += elements[index + 1]
        last_symbol = last_symbol * int(number)
        filtered += last_symbol
        last_symbol = ''
        number = ''
print(f'Unique symbols used: {counter}')
print(filtered)

