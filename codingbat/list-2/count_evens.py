def count_evens(nums):
    """
    Return the number of even ints in the given array.

    Note: the % "mod" operator computes the remainder,
    e.g. 5 % 2 is 1.
    """
    evens = 0
    for number in nums:
        if number % 2 == 0:
            evens += 1
    return evens

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
