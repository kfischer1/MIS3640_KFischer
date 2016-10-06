import random
import turtle

#made the drunkard turtle "arrow" shape to indicated the direction the man is moving
#chaned color to blue and made arrow size smaller
drunkard = turtle.Turtle()
drunkard.color('blue')
drunkard.shape('arrow')
drunkard.turtlesize(.5)
print(drunkard)
def drunkard_walk(x, y, n):
    drunkard.circle(2.5)
    #marks the initial location of the drunkard
    drunkard.position()
    x = 0
    y = 0
    ns = 0
    ew = 0
    ns_direction = ''
    ew_direction = ''
    #used North, South, East and West as the 4 direction options
    for block in range(n):
        direction = random.randrange(0,4)
        #randomizes the direction that the drunkard chooses to walk
        if direction == 0:
            ns += 1
            print('Walks one block North')
            drunkard.setheading(90)
        elif direction == 1:
            ew += 1
            print('Walks one block East')
            drunkard.setheading(0)
        elif direction == 2:
            ns -= 1
            print('Walks one block South')
            drunkard.setheading(270)
        else:
            ew -= 1
            print('Walks one block West')
            drunkard.setheading(180)
        drunkard.fd(35)
        drunkard.stamp()
    if ns >= 0:
        ns_direction = 'North'
    else:
        ns_direction = 'South'
    if ew >= 0:
        ew_direction = 'East'
    else:
        ew_direction = 'West'
    print('After', n,'intersections, he is of %s block(s) to the %s and %s block(s) to the %s from where he started' %(abs(ns), ns_direction, abs(ew), ew_direction))
    while True:
        drunkard.stamp()

drunkard_walk(0,0,20)
print("The drunkard started from (%d,%d)." % (x, y))
distance = drunkard_walk(x,y,n)
print(" After", n, "intersections, he's",
      distance, "blocks from where he started.")
turtle.mainloop()

"""
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
"""