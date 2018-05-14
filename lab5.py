import turtle


def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0

    while n != 1:

        if (n % 2) == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = n * 3 + 1
            # the last print is 1
        count += 1
    return count


def createWorld():
    turtle.setworldcoordinates(0, 0, 10, 10)


def updateWorld(t, x, y, yCurrent, Str):
    turtle.setworldcoordinates(0, 0, x + 10, y + 10)
    t.goto(x, y)
    turtleWrite(t, x, y, str)


def turtleWrite(t, xCurrent, yCurrent, strg):
    t.up()
    t.goto(0, yCurrent)
    t.write(strg, False, align="left")
    t.goto(xCurrent, yCurrent)
    t.down()


def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    bound = 1 + int(input("What is the upper bound of the range? "))
    result = 0
    createWorld()
    max_so_far = 0

    for i in range(1, bound):
        result = seq3np1(i)
        if result > max_so_far:
            max_so_far = result

        currentMaxStr = "Max so far:" + str(i) + ", " + str(max_so_far)
        updateWorld(t, i, max_so_far, result, currentMaxStr)

        # working on turtle write, what am i graphing? Max y or current return? make it write in top left
        # its not writing what i want, the coordinates seem off
        # gl

    wn.exitonclick()


main()
