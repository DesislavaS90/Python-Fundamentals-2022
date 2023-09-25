import re
numbers = input()

regex = r'(^|(?<=\s))[-]?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

result = re.finditer(regex, numbers)

for r in result:
    print(r.group(), end=' ')