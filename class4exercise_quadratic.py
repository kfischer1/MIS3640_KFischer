#Solving a quadratic function
import math
import cmath

#Define the quadratic variables
def quadratic(a,b,c):
   A = (b**2)-(4*a*c)
if A >= 0:
       X1 = ((-b + math.sqrt(A)) / 2*a)
       X2 = ((-b - math.sqrt(A)) / 2*a) 
return X1, X2
else:
    print('No Real Solution')

#output of variables
a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))

#print equation solution(s)
print('results are: ')
print(quadratic(a,b,c))

input()

