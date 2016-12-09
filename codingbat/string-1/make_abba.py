def make_abba(a,b):
    """
    Given two strings, a and b, return the result of putting them together in the order abba,
    e.g. "Hi" and "Bye" returns "HiByeByeHi".
    """
    return a+b+b+a


print(make_abba('Hi', 'Bye'))
print(make_abba('Yo', 'Alice'))
print(make_abba('What', 'Up'))