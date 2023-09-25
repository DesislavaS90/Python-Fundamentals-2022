usernames = input().split(', ')

for name in usernames:
    if 3 <= len(name) <= 16 and name.isalnum() or '-' in name or '_' in name and ' ' not in name:
        print(name)