import re

places = input()
my_destination = []
travel_points = 0

pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'
result = re.findall(pattern, places)

for destination in result:
    my_destination.append(destination[1])
    travel_points += len(destination[1])

print(f"Destinations: {', '.join(my_destination)}")
print(f"Travel Points: {travel_points}")


# You will be given a string representing some places on the map. You have to filter only the valid ones. A valid location is:
# Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
# After the first "=" or "/" there should be only letters (the first must be upper-case, other letters could be upper or lower-case)
# The letters must be at least 3

# Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid.

# After you have matched all the valid locations, you have to calculate travel points. They are calculated by summing the lengths of all the valid destinations that you have found on the map.
# In the end, on the first line, print: "Destinations: {destinations joined by ', '}".
# On the second line, print "Travel Points: {travel_points}".
