numbers = input().split()

lst = []
for num in numbers:
    lst.append(abs(float(num)))
print(lst)