"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""
import random
import turtle # Copy code to make a turtle and set up the window
turtle.setup(600,600,0,0)

t = turtle.Turtle() # Create a turtle named t
t.speed(0)

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    t.pencolor(getRandomColor())
    t.left(50)
    t.forward(20)
    t.right(120)
    t.forward(100)

num_shapes = 8

for i in range(1000):
    make_a_shape(t)
    t.right(360/num_shapes)

turtle.exitonclick()