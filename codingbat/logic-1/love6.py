def love6(a, b):
    """
    The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6.
    Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
    """
    return a == 6 or b == 6 or abs(a - b) == 6 or (a + b) ==6

print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))