import turtle
import math

draw = turtle.Turtle()
print(draw)
#Exercise 3.1
#prints triangles
def triangles(t):
    t.lt(30)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.rt(120)
    t.fd(200)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)

triangles(draw)

draw.lt(60)
triangles(draw)

draw.fd(100)
draw.lt(90)
draw.circle(100)
draw.lt(90)
draw.fd(50)
draw.circle(25)

turtle.mainloop()

'''#Exercise 3.2
import math
import turtle
jerry = turtle.Turtle()

print(jerry)

def polygon(t, n, length): 
    polyline(t, n, length, angle)
    angle= 360/n

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t,r):
    circumference = 2*math.pi*r
    n = 80
    length = circumference/n 
    polygon(t,length, n)
    
def arc(t, r, angle):
    arclength = 2*math.pi*r*angle/360
    n =int(arclength / 2)
    s_angle= float(angle) / n
    s_length= arclength / n
    polyline(t, n, s_length, s_angle)

def petal(t, r, angle):
    for i in range(0,2):
        arc(t, r, angle)
        t.lt(180-angle)

for i in range(0,6):
    petal(jerry, 150, 360/6)
    jerry.lt(360/6)
    
arc(jerry, 150, 360/6)
jerry.lt(60)
circle(jerry,150)

turtle.mainloop()
'''