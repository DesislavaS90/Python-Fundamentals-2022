import re

pattern = r'[\d]+'
line = input()

while line:
    result = re.findall(pattern, line)
    if result:
        print(*result, end=' ')
    line = input()
