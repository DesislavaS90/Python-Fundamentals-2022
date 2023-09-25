pairs_of_words = input(). split(' | ')
words = input().split(' | ')
command = input()

my_dict = {}

for word in pairs_of_words:
    word = word.split(': ')
    element, definition = word[0], word[1]
    if element not in my_dict:
        my_dict[element] = [definition]
    else:
        my_dict[element] += [definition]

if command == 'Test':
    for w in words:
        if w in my_dict:
            print(f'{w}:')
            for value in my_dict[w]:
                print(f' -{value}')

elif command == 'Hand Over':
    for key in my_dict.keys():
        print(key, end=' ')






