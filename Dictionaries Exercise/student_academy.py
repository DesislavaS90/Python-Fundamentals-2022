number = int(input())
dictionary = {}

for student in range(number):
    name = input()
    grade = float(input())

    if name not in dictionary:
        dictionary[name] = []
    dictionary[name] += [grade]

for key, value in dictionary.items():
    average = sum(value) / len(value)
    if average < 4.50:
        continue
    else:
        print(f'{key} -> {average:.2f}')