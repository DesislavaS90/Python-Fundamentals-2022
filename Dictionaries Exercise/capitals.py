countries = input().split(', ')
capitals = input().split(', ')

final = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in final.items():
    print(f'{country} -> {capital}')