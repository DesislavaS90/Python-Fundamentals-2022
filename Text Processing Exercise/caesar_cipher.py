text = input()

new_text = ''

for element in text:
    new_text += chr(ord(element) + 3)

print(new_text)