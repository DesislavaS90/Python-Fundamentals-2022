characters = input().split(', ')

values = {key: ord(key) for key in characters}

print(values)