def palindrome(number):
    for n in number:
        print(n[::-1] == n)


numbers = input().split(', ')
palindrome(numbers)