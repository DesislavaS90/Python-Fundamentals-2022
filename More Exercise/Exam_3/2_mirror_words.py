import re
data = input()
pattern = r'([@#])([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})\1'
result = re.findall(pattern, data)

pairs = 0
mirror = []

if not result:
    print('No word pairs found!')

for word in result:
    pairs += 1
    if word[1][::-1] == word[4]:
        mirror.append(word[1] + ' <=> ' + word[4])

if pairs > 0:
    print(f'{pairs} word pairs found!')

if len(mirror) == 0:
    print('No mirror words!')

else:
    print('The mirror words are:')
    print(', '.join(mirror))


# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# At least 3 characters long each (without the surrounding symbols)
# Made up of letters only

# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a match, and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#

# If you don`t find any valid pairs, print: "No word pairs found!"
# If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# If there are no mirror words, print: "No mirror words!"
# If there are mirror words print:


