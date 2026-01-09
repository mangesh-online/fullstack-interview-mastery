import re

def is_palindrome(s):
    filtered = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return filtered == filtered[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
