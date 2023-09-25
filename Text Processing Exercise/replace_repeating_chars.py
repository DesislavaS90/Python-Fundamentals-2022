some_string = input()

sorted_string = ''
last_letter = ''

for letter in some_string:
    if letter != last_letter:
        sorted_string += letter
        last_letter = letter
print(sorted_string)