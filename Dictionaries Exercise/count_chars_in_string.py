my_dict = {}

word = input().split()
symbols = ''.join(word)

for chr in symbols:
    if chr not in my_dict:
        my_dict[chr] = 0
    my_dict[chr] += 1

for char, occurrences in my_dict.items():
    print(f'{char} -> {occurrences}')