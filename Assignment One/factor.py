# # #Factoring of integers. Write a program that asks the user for an integer and then prints
# # # out all its factors. For example, when the user enters 150, the program should print 2 3 5 5

import math
from math import sqrt

number = int(input('Enter an integer: '))             #command that prompts the user to choose an integer

def factor(x):
    """
     factor takes an integer and returns a list containing the factors of the integer
     1. the function only needs to check the numbers up through the square root of the integer, because any factor
         larger than the square root will have the corresponding factor that is less than the square root 
         (i.e. 25 and 5 for 100)
     2.if the integer can be evenly divided by the number that's being checked, add that number
         as well as the integer divided by that number
     """
    i = 2                               # i = 2 will check is the integer is divisible by 2 (evenly) 
    x = int(x)                          # sets x to be an integer
    factors = [ ]                       #place to store the list of factors
    while i * i <= x:                   # when the factor is less than or equal to the integer squared
        if x % i != 0:
            i += 1
        else:
            x //= i
            factors.append(i)           #adds number being checked
    if x > 1:
        factors.append(x)               # adds number integer is divided by
    return factors                      #returns the list of factors for the given integer
print(factor(number))                   #prints the factor list for the number originally entered by the user



