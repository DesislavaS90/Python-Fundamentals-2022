card = input().split()
count_of_shuffles = int(input())

for i in range(count_of_shuffles):
    final_deck = []
    middle = len(card) // 2
    left_side = card[0: middle]
    right_side = card[middle::]
    for j in range(len(left_side)):
        final_deck.append(left_side[j])
        final_deck.append(right_side[j])
    card = final_deck
print(card)