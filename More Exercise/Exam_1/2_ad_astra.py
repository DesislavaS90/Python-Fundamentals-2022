import re

text = input()
calories = 0

pattern = r'([#|\|])([A-Za-z\s]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1(\d+)\1'

result = re.findall(pattern, text)

for food in result:
    calories += int(food[3])
print(f'You have food to last you for: {calories // 2000} days!')

if calories > 2000:
    for i in result:
        print(f'Item: {i[1]}, Best before: {i[2]}, Nutrition: {i[3]}')


# On the first line of the input, you will be given a text string. You must extract the information about the food and calculate the total calories.

# First, you must extract the food info. It will always follow the same pattern rules:
# It will be surrounded by "|" or "#" (only one of the two) in the following pattern:  #{item name}#{expiration date}#{calories}#   or  |{item name}|{expiration date}|{calories}|
# The item name will contain only lowercase and uppercase letters and whitespace

# The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long
# The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have. Keep in mind that you need 2000kcal a day.
