import turtle
import random


def main():
    window = turtle.Screen()  # window
    window.bgcolor('lightblue')

    michelangelo = turtle.Turtle()  # turtles
    leonardo = turtle.Turtle()
    michelangelo.color('orange')
    leonardo.color('blue')
    michelangelo.shape('turtle')
    leonardo.shape('turtle')

    michelangelo.up()  # reset pos.
    leonardo.up()
    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)

    michelangelo.down()  # pen down to draw path
    leonardo.down()

    x = random.randrange(1, 300)  # method of movement 1
    michelangelo.forward(x)
    x = random.randrange(1, 300)
    leonardo.forward(x)

    michelangelo.up()  # reset pos.
    leonardo.up()
    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)
    michelangelo.clear()
    leonardo.clear()
    michelangelo.down()  # pen down to draw path
    leonardo.down()

    count = 0  # method of movement 2
    while count < 10:  # calls to forward with while loop (I'm lazy)
        x = random.randrange(0, 30)  # call set 1
        michelangelo.forward(x)
        x = random.randrange(0, 30)
        leonardo.forward(x)
        count = count + 1

    michelangelo.up()  # reset pos.
    leonardo.up()

    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)
    michelangelo.clear()
    leonardo.clear()

    window.exitonclick()


main()
