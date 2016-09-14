#quadratic equation ax**2 + bx + c = 0

import math
import cmath

input = a, b, c 


#discriminant function
def quadratic(a, b, c):
    A = b**2 - 4 * a * c
#paramaters to resulting in a solution
if A >= 0:
    X1= ((-b + math.sqrt(A)) / 2*a)
    X2= ((-b - math.sqrt(A)) / 2*a)
    return X1, X2

else:
    print('No solution')


input = a,b,c 

discRoot = cmath.sqrt(b * b - 4 * a * c)
root1 = (-b + discRoot) / (2 * a)
root2 = (-b - discRoot) / (2 * a)

print('The solutions are:', root1 root2)

input()

