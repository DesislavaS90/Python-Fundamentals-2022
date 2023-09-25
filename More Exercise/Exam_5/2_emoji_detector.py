import re

text = input()
pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)'
digits_pattern = r'\d'

emojis = re.findall(pattern, text)
digits = re.findall(digits_pattern, text)

cool_threshold = 1
for n in digits:
    cool_threshold *= int(n)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')

for emoji in emojis:
    emoji_sum = 0
    for chr in emoji[1]:
        emoji_sum += ord(chr)
    if emoji_sum >= cool_threshold:
        print(''.join(emoji))




# An emoji is valid when:
# It is surrounded by 2 characters, either "::" or "**"
# It is at least 3 characters long (without the surrounding symbols)
# It starts with a capital letter
# Continues with lowercase letters only

# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::

# You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that to take all emojis out of the text, count them and print only the cool ones on the console.


