import re

text = input()
pattern = r'(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)\b'

while text:
    result = re.findall(pattern, text)
    if result:
        for link in result:
            print(link[0])
    text = input()
