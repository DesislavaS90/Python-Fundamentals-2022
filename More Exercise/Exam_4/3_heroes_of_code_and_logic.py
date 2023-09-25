number_of_heroes = int(input())

my_heroes = {}

for hero in range(number_of_heroes):
    heroes, hit_points, mana_points = input().split()
    my_heroes[heroes] = [int(hit_points), int(mana_points)]

while True:
    command = input().split(' - ')

    if command[0] == 'End':
        break

    elif command[0] == 'CastSpell':
        hero_name, MP_needed, spell_name = command[1], int(command[2]), command[3]
        if my_heroes[hero_name][1] >= MP_needed:
            my_heroes[hero_name][1] -= MP_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {my_heroes[hero_name][1]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')

    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        my_heroes[hero_name][0] -= damage
        if my_heroes[hero_name][0] > 0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {my_heroes[hero_name][0]} HP left!')
        else:
            del my_heroes[hero_name]
            print(f'{hero_name} has been killed by {attacker}!')

    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])
        diff = 200 - my_heroes[hero_name][1]
        my_heroes[hero_name][1] += amount
        if my_heroes[hero_name][1] > 200:
            my_heroes[hero_name][1] = 200
            print(f'{hero_name} recharged for {diff} MP!')
        else:
            print(f'{hero_name} recharged for {amount} MP!')

    elif command[0] == 'Heal':
        hero_names, amounts = command[1], int(command[2])
        diffs = 100 - my_heroes[hero_names][0]
        my_heroes[hero_names][0] += amounts
        if my_heroes[hero_names][0] > 100:
            my_heroes[hero_names][0] = 100
            print(f'{hero_names} healed for {diffs} HP!')
        else:
            print(f'{hero_names} healed for {amounts} HP!')

for key, value in my_heroes.items():
    print(f'{key}')
    print(f'  HP: {value[0]}\n  MP: {value[1]}')


# "CastSpell – {hero name} – {MP needed} – {spell name}"
# If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
# "{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# If the hero is unable to cast the spell print:
# "{hero name} does not have enough MP to cast {spell name}!"

# "TakeDamage – {hero name} – {damage} – {attacker}"
# Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# "{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# If the hero has died, remove him from your party and print:
# "{hero name} has been killed by {attacker}!"

# "Recharge – {hero name} – {amount}"
# The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200. (the MP can't go over the maximum value).
#  Print the following message:
# "{hero name} recharged for {amount recovered} MP!"

# "Heal – {hero name} – {amount}"
# The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
#  Print the following message:
# "{hero name} healed for {amount recovered} HP!"
