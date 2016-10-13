# names = ['Rose', 'Jerry', 'Alex']
# scores = [95, 75, 85]
# i = names.index('Jerry')
# print(scores[i])

# prints the two names and corresponding grade
grades = {'Jerry': 75, 'Rose': 95}
print(grades['Jerry'])

#includes brian and prints grades
grades['Brian'] = 90
print(grades)
#defines length of grades as 3 (3 different grades)
print(len(grades))
print('Jerry' in grades)
print(90 in grades.values())


def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookkeeper')
print(h)

#creates a histogram for the work, counting how many times each letter in the word occurs


#The raise statement causes an exception; in this case it causes a LookupError, which is a built-in exception used to indicate that a lookup operation failed.
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()
    