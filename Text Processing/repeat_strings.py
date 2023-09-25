strings = input().split()

# final = [word * len(word) for word in strings]
final = []
for word in strings:
    final += word * len(word)
print(''.join(final))
