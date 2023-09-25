word = input()

vowels = ['a', 'o', 'u', 'e', 'i']

no_vowels = [element for element in word if element.lower() not in vowels]

print(''.join(no_vowels))