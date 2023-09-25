import re

count_of_string = int(input())

for string in range(count_of_string):
    data = input()
    pattern = r'(\!)([A-Z][a-z]{2,})\1\:[\[]([A-Za-z]{7,})\]'
    result = re.findall(pattern, data)
    if not result:
        print('The message is invalid')

    else:
        for element in result:
            my_elements = []
            for chr in element[2]:
                my_elements.append(str(ord(chr)))
            print(f"{element[1]}: {' '.join(my_elements)}")
