import lsystems


def main():

    axiom = input("Please input an axiom: ")
    iterations = int(input("Please input the number of iterations: "))
    angle = int(input("Please input the angle: "))
    distance = int((input("Please input the distance: ")))
    number_of_rules = int(input("Please input the number of rules: "))
    rules = ''

    for i in range(number_of_rules):
        current_rule = input("Please input a rule (Format:'character:substitution:'): ")
        rules += current_rule + ','

    result = lsystems.createLSystem(iterations, axiom, rules)
    print(result)
    lsystems.drawLSystem(result, distance, angle)
    print("it worked!")

# test with: AB , 3, 60, 30, 1, A:AF+FB+FF-FAB

main()
