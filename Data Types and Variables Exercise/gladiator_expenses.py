lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

money_counter = 0

broken_helmet = lost_fights // 2
broken_sword = lost_fights // 3
broken_shield = lost_fights // 6
broken_armor = broken_shield // 2

expenses = helmet_price * broken_helmet + sword_price * broken_sword + shield_price * broken_shield\
           + armor_price * broken_armor

print(f'Gladiator expenses: {expenses:.2f} aureus')