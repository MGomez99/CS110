from lab11 import lsystems
import turtle


def main():
    files = ["fakename.txt", "arrowheadcurve.txt", "dragoncurve.txt", "hilbertcurve.txt", "peanogospercurve.txt",
             "sierpinskitrianglecurve.txt"]

    for file in files:
        try:
            current_system = lsystems.Lsystem(file)
            result = current_system.createLSystem(current_system.iterations, current_system.axiom, current_system.rules)
            print("Result:", result)
            current_system.drawLSystem(result, current_system.angle)
        except FileNotFoundError:
            print(file, "doesn't exist. Skipping file.\n")
            continue


main()
