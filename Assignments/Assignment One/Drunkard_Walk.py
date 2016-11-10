import random
import turtle
import math
drunkard = turtle.Turtle()
drunkard.shape('turtle')
drunkard.turtlesize(.5,.5,.5)
print(drunkard)

def drunkWalk(n):
    """
    the drunkard function takes n, the number of moves the drunkard will take
    1. create variables for the north/south and east/west directions
    2. create variables for the direction of the drunkard at the end of his journey
    3. for n moves, a random number between 0 and 4 is generated - each corresponds to a cardinal direction
        a. the north/south or east/west value is changed depending on the generated number
        b. the direction is printed for the User
        c. set the turtle's heading to that direction and move it forward
        d. stamp the turtle's shape so the user can see where it is going'
    4. the final directions from the origin are translated
    """
    #draw a circle so that I can see the origin
    drunkard.circle(5)                  #drawing circle to start to signify the origin
    ns = 0                              # this will set the direction variables as 0 
    ew = 0
    ns_direction = ''
    ew_direction = ''
    for block in range(n):                          # for loop for the number of blocks that the drunkard walks
        direction = random.randrange(0,4)           # this will pick a random direction of the 4 options for each block walked (NSEW)
        if direction == 0:
            ns += 1                                 # will show drunkark walking in North direction and it will be printed
            print('The drunkard walks North')
            drunkard.setheading(90)                 #sets the direction of the turtle/ drunkard at a 90 degree angle
        elif direction == 1:
            ew += 1                                 # given this situation, the drunkard will go East
            print('The drunkard walks East')
            drunkard.setheading(0)                  # sets the turn back to 0 as he will be going East
        elif direction == 2:
            ns -= 1
            print('The drunkward walks South')      #random pick walking South turns the direction of the turtle 270 degrees to make him face south
            drunkard.setheading(270)
        else:
            ew -= 1
            print('The drunkard walks West')        #all else, he is going West which the angle the turtle moves to head this way will be 180
            drunkard.setheading(180)
        drunkard.fd(25)                             #each time the drunkard walks in a direction he will go 25 units forward
        drunkard.stamp()                              # the stamp will track where the drunkard has walked along the way
    if ns >= 0:
        ns_direction = 'North'                  #differentiating NS direction into two ( north and south )
    else:
        ns_direction = 'South'
    if ew >= 0:                                 # when EW is 0 it is East, otherwise he goes West
        ew_direction = 'East'
    else: 
        ew_direction = "West"
    print('The drunkard has walked a total distance of %s blocks to the %s and %s blocks to the %s' %(abs(ns), ns_direction, abs(ew), ew_direction))
    while True:
        drunkard.lt(2)

drunkWalk(70)

turtle.mainloop()