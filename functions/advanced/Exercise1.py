

def is_palindrome(str):
    """function that accepts a string and returns True if the string is a palindrome. Otherwise, False."""
    it_is = False
    if str == str[::-1]:
        it_is = True
    return it_is

help(is_palindrome)
print(is_palindrome("radar"))
print(is_palindrome("world"))