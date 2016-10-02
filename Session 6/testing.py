
import random
import turtle
import math
jerry = turtle.Turtle()
#jerry.shape('turtle')
#jerry.turtlesize(.5,.5,.5)
print(jerry)
def drunkard_walk(n):
#     """
#     the drunkard function takes n, the number of moves the drunkard will take
#     1. create variables for the north/south and east/west directions
#     2. create variables for the direction of the drunkard at the end of his journey
#     3. for n moves, a random number between 0 and 4 is generated - each corresponds to a cardinal direction
#         a. the north/south or east/west value is changed depending on the generated number
#         b. the direction is printed for the User
#         c. set the turtle's heading to that direction and move it forward
#         d. stamp the turtle's shape so the user can see where it is going'
#     4. the final directions from the origin are translated
#     """
#     #draws a circle so the user can see the origin
    jerry.circle(5)
    ns = 0
    ew = 0
    ns_direction = ''
    ew_direction = ''
    for block in range(n):
        direction = random.randrange(0,4)
        if direction == 0:
            ns += 1
            print('The drunkard walks North')
            jerry.setheading(90)
        elif direction == 1:
            ew += 1
            print('The drunkard walks East')
            jerry.setheading(0)
        elif direction == 2:
            ns -= 1
            print('The drunkard walks South')
            jerry.setheading(270)
        else:
            ew -= 1
            print('The drunkard walks West')
            jerry.setheading(180)
        jerry.fd(30)
        jerry.stamp()
    if ns >= 0:
        ns_direction = 'North'
    else:
        ns_direction = 'South'
    if ew >= 0:
        ew_direction = 'East'
    else:
        ew_direction = 'West'
    print('The drunkard has moved a total distance of %s block(s) to the %s and %s block(s) to the %s' %(abs(ns), ns_direction, abs(ew), ew_direction))
    #slowly rotate the turtle so the user can see where it ended up
    while True:
        jerry.lt(2)

drunkard_walk(20)
distance = drunkard_walk(x,y,n)
print(" After", n, "intersections, he's",
      distance, "blocks from where he started.")
turtle.mainloop()

