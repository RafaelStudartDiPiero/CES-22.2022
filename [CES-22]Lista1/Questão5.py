def is_palindrome(s):
    s = s.strip().lower()
    return s == s[::-1]


# Example

result = is_palindrome("Ana")
if result:
    print("Palíndromo")
else:
    print("Não Palíndromo")
