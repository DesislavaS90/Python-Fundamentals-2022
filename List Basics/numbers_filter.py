n = int(input())

numbers = []
my_numbers = []


for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()
for j in numbers:
    filtered = ((command == 'even' and j % 2 == 0) or (command == 'odd' and j % 2 != 0) or
          (command == 'positive' and j >= 0) or (command == 'negative' and j < 0))
    if filtered:
        my_numbers.append(j)

print(my_numbers)


