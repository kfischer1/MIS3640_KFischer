
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
    forward = 0
    left = 0
    forward_direction = ''
    left_direction = ''
    #used 'forward and 'left as the 2 directions: when forward= false (walks backwards) & when left= false (walks right)
    for block in range(n):
        direction = random.randrange(0,4)
        #randomizes the direction that the drunkard chooses to walk
        if direction == 0:
            forward += 1
            print('Forward')
            drunkard.setheading(90)
        elif direction == 1:
            left += 1
            print('Left')
            drunkard.setheading(0)
        elif direction == 2:
            forward -= 1
            print('Backward')
            drunkard.setheading(270)
        else:
            left -= 1
            print('Right')
            drunkard.setheading(180)
        drunkard.fd(35)
        drunkard.stamp()
    if forward >= 0:
        forward_direction = 'Forward'
    else:
        forward_direction = 'Backward'
    if left >= 0:
        left_direction = 'Left'
    else:
        left_direction = 'Right'
    print('After', n,'intersections, he is of %s block(s) to the %s and %s block(s) to the %s from where he started' %(abs(forward), forward_direction, abs(left), left_direction))
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