def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0].lower() == s[-1].lower() and is_palindrome(s[1:-1])


s=input("Enter a string: ")
if is_palindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
# Example: is_palindrome("racecar") should return True
