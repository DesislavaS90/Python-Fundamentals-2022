def validator(given_password):
    correct = True
    if 6 > len(given_password) or len(given_password) > 10:
        correct = False
        print('Password must be between 6 and 10 characters')
    if not given_password.isalnum():
        correct = False
        print('Password must consist only of letters and digits')
    digit = 0
    for i in given_password:
        if i.isdigit():
            digit += 1
    if digit < 2:
        correct = False
        print('Password must have at least 2 digits')
    if correct:
        print('Password is valid')


password = input()
validator(password)