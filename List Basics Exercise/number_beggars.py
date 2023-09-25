money = input().split(', ')
beggar = int(input())

money_list = []
index = 0

for i in range(beggar):
    beggars = 0

    for current_index in range(index, len(money), beggar):
        beggars += int(money[current_index])

    money_list.append(beggars)

    index += 1
print(money_list)
