import turtle


def seq3np1(n):
    """
    Print the 3n+1 sequence from n, terminating when it reaches 1.
    :param n: An integer to be reduced to 1
    :return: How many iterations it takes to make n 1 using the 3n+1 sequence
    """
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
    """
    Sets up world coordinates
    Takes no parameters
    :return: none
    """
    turtle.setworldcoordinates(0, 0, 10, 10)


def updateWorld(t, t2, x_current, y_current, y_max, text):
    """
    This function will draw the graph of the current number in the list vs resulting number of iterations to get to 1
    :param t: turtle that draws the graph
    :param t2: turtle that will write the max so far
    :param x_current: current x
    :param y_current: current y
    :param y_max: aka max_so_far
    :param text: string that was created in main, states max y - used for writing
    :return: none
    """
    turtle.setworldcoordinates(0, 0, x_current + 10, y_max + 10)

    t2.up()
    t2.goto(0, y_max)
    t.goto(x_current, y_current)

    turtleWrite(t2, y_max, text)


def turtleWrite(t2, y_max, text):
    """
    Writes the max_so_far string on the top left corner of the graph
    :param t2: turtle that will do the writing
    :param y_max: Max height of the graph - 10
    :param text: string that will be written on the graph
    :return: none
    """
    t2.clear()

    t2.write(text, False, align="left")


def main():
    t = turtle.Turtle()
    t2 = turtle.Turtle()  # Turtle that will write the max
    t.speed(0)
    t2.speed(0)
    t2.up()
    wn = turtle.Screen()
    bound = 1 + int(input("What is the upper bound of the range? "))  # Make the range "inclusive"

    createWorld()
    max_so_far = 0  # initialize the max

    for i in range(1, bound):
        result = seq3np1(i)
        if result > max_so_far:
            max_so_far = result
            # If the result is our new max, update the variable max_so_far

        current_max_str = "Max so far: (" + str(i) + "," + str(max_so_far) + ")"  # for writing purposes
        t2.hideturtle()  # for whatever reason, the only way I could hide t2 was to put it here
        updateWorld(t, t2, i, result, max_so_far, current_max_str)

    wn.exitonclick()


main()
