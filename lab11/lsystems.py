import turtle


class Lsystem:
    def __init__(self, filename):
        """
        init
        :param filename: name of file
        """
        file = open(filename, "r")
        lines = []
        for line in file:
            lines.append(line)

        self.angle = int(lines.pop(0).rstrip('\n'))

        print("Angle:", self.angle)
        self.iterations = int(lines.pop(0).rstrip('\n'))
        print("Iter:", self.iterations)
        self.axiom = lines.pop(0)
        print("Axiom:", self.axiom)
        self.rules = [line.replace("\n", "").replace(" ", "") for line in lines]
        print("Rules:", self.rules)
        file.close()

    def applyRules(self, char, rules):
        """
        changes char based on rules
        :param char: char in string
        :param rules: rules to change char
        :return: changed/unchanged char
        """
        for rule in rules:
            rule = rule.split(':')
            if char == rule[0]:
                char = rule[1]
                return char

        return char 
 
    def processString(self, axiom, rules):
        """
        creates a new string with the new chars
        :param axiom: string to be changed
        :param rules: rules to change string
        :return: new string
        """
        string_final = ''
        for char in axiom:
            string_final += self.applyRules(char, rules)
        return string_final

    def createLSystem(self, iterations, axiom, rules):
        """
        creates final axiom based on iterations
        :param iterations: number of times to process string
        :param axiom: string to be changed
        :param rules: rules to change string
        :return: finalized axiom
        """
        for i in range(iterations):
            axiom = self.processString(axiom, rules)
        return axiom

    def drawLSystem(self, axiom, degree):
        """
        draws lsystem based on axiom
        :param axiom: finalized axiom
        :param degree: degree to turn
        :return: none
        """
        t = turtle.Turtle()
        t.speed(0)
        t.pencolor("red")
    
        for char in axiom:
            if char == 'F':
                t.fd(5)
            elif char == '+':
                t.rt(degree)
            elif char == '-':
                t.lt(degree)
        print("Done with this System!\n\n")
        t.reset()
        t.ht()


