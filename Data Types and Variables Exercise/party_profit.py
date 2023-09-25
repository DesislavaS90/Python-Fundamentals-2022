people = int(input())
days = int(input())

coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        people -= 2
    if i % 15 == 0:
        people += 5
    if i % 3 == 0:
        coins -= 3 * people
    if i % 5 == 0:
        coins += 20 * people
        if i % 3 == 0:
            coins -= 2 * people
    coins += 50
    coins -= 2 * people
coins_per_person = int(coins / people)
print(f'{people} companions received {coins_per_person} coins each.')



