string_to_remove = input()
second_string = input()

while string_to_remove in second_string:

    second_string = second_string.replace(string_to_remove, '')
print(second_string)