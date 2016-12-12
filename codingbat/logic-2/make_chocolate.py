def make_chocolate(small, big, goal):
    """
    We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
    Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't
    be done.
    """
    maxBig = goal / 5
   
    if big >= maxBig:
        if small >= (goal - maxBig * 5):
            return goal - maxBig * 5
    if big < maxBig:
        if small >= (goal - big * 5):
            return goal - big * 5
    return -1

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))