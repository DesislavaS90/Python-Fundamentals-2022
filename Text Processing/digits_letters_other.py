some_string = input()

letters = ''
digits = ''
other = ''

for element in some_string:
    if element.isdigit():
        digits += element
    elif element.isalpha():
        letters += element
    else:
        other += element
print(digits)
print(letters)
print(other)