path = input().split('\\')

extension = path[-1].split('.')

print(f'File name: {extension[0]}')
print(f'File extension: {extension[1]}')
