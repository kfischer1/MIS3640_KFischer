import turtle

'''
#Exercise 2.1
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

    
# Exercise 2.2
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
'''

# Exercise 2.3
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


#Exercise 2.4
import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

jerry = turtle.Turtle()

circle(jerry, 40) 

#square(jerry,100)
#polygon(jerry, 50, 4)
#square(jerry,100)

alex = turtle.Turtle()
#polygon(alex, 30, 8)
#polygon(alex, n=7, length=70)
#polygon(alex, 70, 7)


turtle.mainloop()



