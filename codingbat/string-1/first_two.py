def first_two(str):
    """
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
    If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty
    string "" yields the empty string "".
    """
    if len(str)<= 2:
        return str
    return str[:2]

print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))