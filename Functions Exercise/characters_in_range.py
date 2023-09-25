def characters(first_string, second_string):
    my_lst = []
    for i in range(ord(first_string) + 1, ord(second_string)):
        my_lst.append(chr(i))
    return ' '.join(my_lst)


first_char = input()
second_char = input()
print(characters(first_char, second_char))