str_1 = 'iPAD'
str_2 = 'Babson'
str_3 = 'python'

#return ends the whole function (true, false, true: looking at first letter of string only)
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1(str_1))
print(any_lowercase1(str_2))
print(any_lowercase1(str_3))

# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'


# is checking the last letter of the string-- flag is updated for each iteration to follow
# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag

# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

    #False, False, True