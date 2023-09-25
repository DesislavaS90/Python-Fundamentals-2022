secret_message = input().split()

filter_list = []
digit = []
final = []

for word in secret_message:
    for letter in word:
        if letter.isdigit():
            digit += letter
        else:
            filter_list.append(letter)
    digits = ''.join(digit)
    digit = chr(int(digits))
    filter_list.insert(0, ''.join(digit))
    filter_list[1], filter_list[-1] = filter_list[-1], filter_list[1]
    final.append(''.join(filter_list))
    digit = []
    filter_list = []

print(' '.join(final))