import turtle
import random


def applyRules(char, rules):
    """
    takes char, applies rules, returns char
    :param: char (character from axiom) [char]
    :param: rules (rules to modify char) [list]
    return char
    """

    rules = rules.split(',')
    rules = rules[:-1]  # trim trailing comma
    num_rules = len(rules)  # will return the number of rules

    # what if there's two rules?
    rule_one = rules[0]  # first rule
    r1 = rule_one.split(':')  # splits into input, output

    if num_rules == 2:
        rule_two = rules[1]
        r2 = rule_two.split(':')

    if char == r1[0]:
        char = r1[1]  # change to the rule

        return char
    elif num_rules == 2:
        if char == r2[0]:
            char = r2[1]
        return char
    else:
        return char


def processString(axiom, rules):
    """
    calls applyRules to change each character in the axiom
    :param: axiom (string to be changed) [string]
    :param: rules (rules to modify axiom) [list]
    returns string_final
    """
    string_final = ''
    for char in axiom:
        string_final += applyRules(char, rules)

    return string_final
    # takes each char in axiom and calls apply rules, adds to string_final


def createLSystem(iterations, axiom, rules):
    """
    changes the axiom by calling process string for a given number of iterations
    :param: iterations (number of times to change axiom) [int]
    :param: axiom (string to be changed) [string]
    :param: rules (list of rules to be applied) list]
    return axiom
    """

    for i in range(iterations):
        axiom = processString(axiom, rules)
    print(axiom)
    return axiom
    # takes the axiom and calls process string to change the axiom based on rules, for a certain amount of iterations


def drawLSystem(orders, distance, degree):
    """
    uses turtle to draw the result based on a set rule
    :param: orders (char in result) [char]
    :param: distance (distance to go forward when prompted) [int]
    :param: degree (degrees to turn when prompted) [int]
    return none    
    """

    t = turtle.Turtle()
    t.speed(0)
    t.pencolor("red")
    wn = turtle.Screen()

    for order in orders:
        if order == 'F':
            t.pensize(random.randrange(1, 11))
            t.fd(distance)
        elif order == '+':
            t.color("blue")
            t.rt(degree)
        elif order == '-':
            t.color("green")
            t.lt(degree)

    wn.exitonclick()
