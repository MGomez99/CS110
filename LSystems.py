import turtle


def processString(mystr):
    newstr = ""
    for c in mystr:
        if c == "F":
            newstr += "F-F++F-F"
        else:
            newstr += c
    return newstr


def createLSystem(num, axiom):
    for i in range(num):
        axiom = processString(axiom)

    return axiom


def visualize(result, angle, distance):
    t = turtle.Turtle()
    t.speed(0)
    wn = turtle.Screen()
    for order in result:
        if order == 'F':
            t.fd(distance)
        if order == '+':
            t.rt(angle)
        if order == '=':
            t.lt(angle)
    wn.exitonclick()


def main():
    """
    L-Systems:
    Axiom, Rules → Transformations
    Iterations
    """
    i = int(input("How many iterations?: "))
    result = createLSystem(i, "F")

    angle = int(input("Angle?: "))
    distance = int(input("Distance?: "))
    visualize(result, angle, distance)


main()
