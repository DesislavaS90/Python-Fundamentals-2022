first_string = input().split(', ')
second_string = input().split(', ')

substrings = []

for first in first_string:
    for second in second_string:
        if first in second and not first in substrings:
            substrings.append(first)

print(substrings)

