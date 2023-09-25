def ispalindrome(elements):
    palindrome_lst = [i for i in elements if i == i[::-1]]
    return palindrome_lst


words = input().split()
palindrome = input()

number = ispalindrome(words).count(palindrome)

print(ispalindrome(words))
print(f"Found palindrome {number} times")