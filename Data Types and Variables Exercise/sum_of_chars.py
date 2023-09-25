characters = int(input())

counter = 0

for i in range(characters):
    current_chr = input()
    counter += ord(current_chr)

print(f'The sum equals: {counter}')