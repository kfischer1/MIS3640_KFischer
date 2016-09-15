#Solving a quadratic function
import math
import cmath

#Define the quadratic variables
def quadratic(a,b,c):
    discriminant = (b**2)-(4*a*c)
    if discriminant < 0:
        print('No Real Solution')
    if discriminant == 0:
        solution = -b / (2*a)
        print('One Solution:', solution)
    else:
        solution_one = (-b + math.sqrt(discriminant)) / (2*a) 
        solution_two = (-b - math.sqrt(discriminant)) / (2*a) 
        print('Two Solutions:', solution_one,'or', solution_two)
#output of variables
a = float(input('Enter coefficient for a:'))
b = float(input('Enter coefficient for b:'))
c = float(input('Enter coefficient for c:'))

#print equation solution(s)

print(quadratic(a,b,c))

input()

