number_of_cars = int(input())

my_cars = {}

for car in range(number_of_cars):
    cars = input().split('|')
    my_cars[cars[0]] = [int(cars[1]), int(cars[2])]

while True:
    command = input().split(' : ')

    if command[0] == 'Stop':
        break

    elif command[0] == 'Drive':
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if my_cars[car][1] < fuel:
            print(f'Not enough fuel to make that ride')
        else:
            my_cars[car][1] -= fuel
            my_cars[car][0] += distance
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if my_cars[car][0] >= 100000:
                del my_cars[car]
                print(f'Time to sell the {car}!')

    elif command[0] == 'Refuel':
        car, fuel = command[1], int(command[2])
        diff = 75 - my_cars[car][1]
        my_cars[car][1] += fuel
        if my_cars[car][1] > 75:
            my_cars[car][1] = 75
            print(f'{car} refueled with {diff} liters')
        else:
            print(f'{car} refueled with {fuel} liters')

    elif command[0] == 'Revert':
        car, kilometers = command[1], int(command[2])
        my_cars[car][0] -= kilometers
        if my_cars[car][0] < 10000:
            my_cars[car][0] = 10000
            continue
        print(f'{car} mileage decreased by {kilometers} kilometers')

for key, value in my_cars.items():
    print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')


# "Drive : {car} : {distance} : {fuel}":
# You need to drive the given distance, and you will need the given fuel to do that. If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
# If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel, and print:  "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: "Time to sell the {car}!"

# "Refuel : {car} : {fuel}":
# Refill the tank of your car.
# Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up.
# Print a message in the following format: "{car} refueled with {fuel} liters"

# "Revert : {car} : {kilometers}":
# Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format: "{car} mileage decreased by {amount reverted} kilometers"
# If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and  DO NOT print anything.
