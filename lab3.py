import math
import turtle
import random


# sine function drawing
def sineFn(y, trtl):
    for i in range(y):
        y = math.sin(math.radians(i))
        print(y)
        trtl.goto(i, y)


# sets bg color and world coordinates
def setUpWindow(wn, x):
    wn.bgcolor("green")
    turtle.setworldcoordinates(-x, -1, x, 1)


# draws axis and places turtle in starting place
def setUpTurtle(t):
    t.setpos(0, 0)
    t.color("black")

    for i in range(4):
        t.forward(1)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.lt(90)


def main():
    wn = turtle.Screen()  # window
    luke = turtle.Turtle()  # turtle
    x = math.radians(360)  # 360 degrees in rads

    setUpWindow(wn, x)
    setUpTurtle(luke)

    sineFn(361, luke)  # calls sine function to draw a sine curve

    wn.exitonclick()


main()
