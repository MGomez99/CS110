'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(turtle, width, top_left_x, top_left_y) - to outline dartboard
  drawLine(turtle, x_start, y_start, x_end, y_end) - to draw axes
  drawCircle(turtle, radius) - to draw the circle
  setUpDartboard(screen, turtle) - to set up the board using the above functions
  inCircle(turtle, circle_center, radius) - determine if dot is in circle
  throwDart(turtle)
  montePi(turtle, num_darts) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

# List constants here (NO MAGIC NUMBERS!):
BATCH_OF_DARTS = 5000
BOARD_WIDTH = 2
RIGHT_ANGLE = 90

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(t, width, top_left_x, top_left_y):
    t.up()
    t.goto(top_left_x,top_left_y)
    t.down()
    
    for i in range(4):
        t.forward(width)
        t.rt(90)
    
    t.up()
    t.home()
   

def drawLine(t, x_start, y_start, x_end, y_end):

    t.down()

    t.goto(x_start, 0)
    t.goto(x_end,0)
    t.goto(0,0)
    t.goto(0,y_start)
    t.goto(0,y_end)
    t.goto(0,-1)
    
    t.up()


def drawCircle(t, radius):

    t.down()
    t.circle(radius, steps=360)
    t.up()


def setUpDartboard(window, t):
    
    window.setworldcoordinates(-1, -1, 1, 1)
    drawSquare(t, BOARD_WIDTH, -1, 1)
    drawLine(t, -1, -1, 1, 1)
    drawCircle(t, 1)

def throwDart(t):
    x_throw = random.uniform(0,1)
    y_throw = random.uniform(0,1)
    t.shape("circle")
    t.up()
    t.goto(x_throw,y_throw)
    t.stamp()
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)

    print("\tPart A Complete...")
    print("=========== Part B ===========")
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(number_darts, darty)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
