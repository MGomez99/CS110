import turtle


def applyRules(char, rules):
    # takes char, applies rules, returns char

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
    string_final = ''
    for char in axiom:
        string_final += applyRules(char, rules)

    return string_final
    # takes each char in axiom and calls apply rules, adds to string_final
        

def createLSystem(iterations, axiom, rules):

    for i in range(iterations):
        axiom = processString(axiom, rules)
    print(axiom)
    return axiom
    # takes the axiom and calls process string to change the axiom based on rules, for a certain amount of iterations


def drawLSystem(orders, distance, degree):

    t = turtle.Turtle()
    t.speed(0)
    wn = turtle.Screen()
    positions = []  # keep track of positions, record (grouping of rel data)

    for order in orders:
        if order == 'F':
            t.fd(distance)
        elif order == '+':
            t.rt(degree)
        elif order == '-':
            t.lt(degree)
        elif order == '[':
            positions.append([t.heading(), t.xcor(), t.ycor()])
        elif order == ']':
            if len(positions) == 0:
                pos = positions.pop(0)
                t.goto(pos[1], pos[2])
                t.setheading(pos[0])

    wn.exitonclick()




