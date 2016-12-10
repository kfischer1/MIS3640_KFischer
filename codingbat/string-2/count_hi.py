def count_hi(str):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            count += 1
    return count

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))