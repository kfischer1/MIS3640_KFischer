#Factoring of integers. Write a program that asks the user for an integer and then prints
# out all its factors. For example, when the user enters 150, the program should print 2 3 5 5

import math
from math import sqrt

i = float(input('Please enter an integer: '))

def factor(n):
    factor_list = []
    n = int(n)
    for num in range(1, int(sqrt(n)+1)):
        if n % num == 0:
            factor_list.append(num)
            factor_list.append(int(n / num))
    return factor_list

print('The factors are: ',factor(i))