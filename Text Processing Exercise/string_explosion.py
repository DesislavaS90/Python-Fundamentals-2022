my_string = input()
counter = 0

filtered = ''

for index in range(len(my_string)):
    if counter > 0 and my_string[index] != '>':
        counter -= 1
    elif my_string[index] == '>':
        filtered += my_string[index]
        counter += int(my_string[index + 1])
    else:
        filtered += my_string[index]

print(filtered)





