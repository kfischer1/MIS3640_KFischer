def sum13(nums):
    """
    Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very
    unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    if len(nums) == 0:
        return 0

    for i in range(0, len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i+1 < len(nums): 
                nums[i+1] = 0
    return sum(nums)

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))