import re

pattern = r'\b_([A-Za-z0-9]+)\b'
sentence = input()
result = re.findall(pattern, sentence)
print(','.join(result))
