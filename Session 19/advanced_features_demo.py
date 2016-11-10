import math

# x = float(input())              
# # if x > 0:
# #     y = math.log(x)
# # else:
# #     y = float('nan') # a special floating-point value that represents “Not a Number”. 
# # print(y)

# y = math.log(x) if x > 0 else float('nan')  
# print(y)
#     #simplifies code (if else into one line)

# LIST COMPREHENSIONS
# # def capitalize_all(t):
# #     res = []
# #     for s in t:
# #         res.append(s.capitalize())
# #     return res
# # a = 'babson'
# # using list comprehension
# def capitalize_all(t):
#     return [s.capitalize() for s in t]

# a = 'Babson College'
# print(capitalize_all(a))


# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#     return res
# print(only_upper(a))
# # using list comprehension
# def only_upper(t):
#     return [s for s in t if s.isupper()]

# #GENERATOR EXPRESSIONS
# L = [x * x for x in range(5)]
# L
# print(L)

# # a generator expression            # generates a number without using memory
# g = (x * x for x in range(5))
# g
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#'yield' can be used to write a Generator 
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# f = fib(4)
# f
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

#ANY AND ALL: among a list or collectors of anything (if in list it will return true)
any([False, False, True])
any(letter == 's' for letter in 'babson')   #function




