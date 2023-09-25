n = int(input())
main_word = input()

lst = []
filtered = []

for i in range(n):
    word = input()
    lst.append(word)
    if main_word in word:
        filtered.append(word)

print(lst)
print(filtered)