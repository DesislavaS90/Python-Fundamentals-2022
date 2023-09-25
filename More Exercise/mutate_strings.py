first_string = input()
second_string = input()

last_printed = first_string
for i in range(len(first_string)):

    word_left = second_string[:i + 1]
    word_right = first_string[i + 1:]
    word = word_left + word_right
    if word == last_printed:
        continue
    print(word)
    last_printed = word











