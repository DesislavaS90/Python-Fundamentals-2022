def loading_bar(n):
    if n == 100:
        return '100% Complete! \n [%%%%%%%%%%]'
    return f'{n}% [{"%" * (n // 10)}{"." * (10 - number // 10)}]\nStill loading...'


number = int(input())
print(loading_bar(number))