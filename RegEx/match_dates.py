import re
dates = input()

date_pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'
match = re.findall(date_pattern, dates)

for m in match:
    print(f'Day: {m[0]}, Month: {m[2]}, Year: {m[3]}')
