"""This program will allow a user to choose from a variety of shapes and
calculate them."""
# Shape Calculator
# Hello this program will ask for what shape you'd like to calculated
import math

__AUTHOR__ = "Christian Lindo"


# Used in order to run math.pi

def circle_diameter_circumference_area(radius):
    """
    :param radius: Asks for input of the radius of a circle
    """
    circumference = 2 * (math.pi * radius)
    diameter = radius * 2
    area = math.pi * (radius ** 2)
    print("Your circle's dimensions are as followed:", "\nCircumference:",
          format(circumference, '.2f'), "\nRadius:", format(radius, '.2f'),
          "\nDiameter:", format(diameter, '.2f'), "\nArea:",
          format(area, '.2f'))


def square_area_perimeter(side_l, side_w):
    """

    :param side_l:
    :param side_w:
    """
    area = side_l * side_w
    perimeter = (side_l * 2) + (side_w * 2)
    print("Your area is:", format(area, '.2f'), "\nYour perimeter is:",
          format(perimeter, '.2f'))


def triangle_area_perimeter_height(side1, side2, side3, angle):
    """

    :param side1:
    :param side2:
    :param side3:
    :param angle:
    """
    area = (side1 * side2) * (math.sin(angle) / 2)
    height = 2 * (area / side1)
    perimeter = side1 + side2 + side3
    print("Your area is:", format(area, '.2f'), "\nYour height is:",
          format(height, '.2f', ), "\nYour perimeter is:",
          format(perimeter, '.2f'))


def misc(name, number):
    """
Asks for input for name generator
    :param name:
    :param number:
    """
    if not number <= 100 and number >= 1:
        # Using "not" and "and" in order to run a test to make sure
        # value matches as asked in the prompt.
        print("Invalid number, try again!")
        number = int(input("Pick a number between 1-100: "))  #
    for x in range(0, number):
        print(name, sep='', )


def main():
    """
Asks for a selection and repeats when computation is complete
    """
    selection = 0
    done = 0
    print("Hello user and welcome to my shape calculator program!")
    print(
        "Use the pro" + "gram as much as you like! When you are finished, "
                        "input "
        # ^ Used a string operator to combine "pro gram"
                        "(5) to quit")
    while done != 1:
        while selection <= 4:
            if selection == 0:
                print("1. Square")
                selection += 1
            elif selection == 1:
                print("2. Circle")
                selection += 1
            elif selection == 2:
                print("3. Triangle")
                selection += 1
            elif selection == 3:
                print("4. Misc")
                selection += 1
            else:
                print("5. Done")
                selection += 1
        while True:
            try:
                shape = int(input(
                    "What shape would you like to calculate?\nPick a number "
                    "from the following choices: "))
                break
            except ValueError:
                print("Error, chose a valid number from the choices.")
        # asks what calculation it would like to run
        while shape > 5 or shape < 1:
            print("Invalid, Try Again")
            while True:
                try:
                    shape = int(input(
                        "What shape would you like to calculate?\nPick a "
                        "number "
                        " from the following choices: "))
                    break
                except ValueError:
                    print("Error, select a proper selection.")
        if shape == 1:
            print("You have chosen Square!")
            while True:
                try:
                    side1 = float(input("Input Side Length: "))
                    break
                except ValueError:
                    print("Error, not a number try again.")
            while True:
                try:
                    side2 = float(input("Input side Width: "))
                    break
                except ValueError:
                    print("Error, not a number try again.")
                    # ask for input of numbers
            square_area_perimeter(side1, side2)  # define statement for output
            selection -= selection
            # Resets list choices and reruns input selection
            # output calculation requested and restarts program
        elif shape == 2:
            print("You have chosen Circle!")
            while True:
                try:
                    radius = float(input("Please enter the radius of the "
                                         "circle: "))
                    break
                except ValueError:
                    print("Error, not a proper value.")
            circle_diameter_circumference_area(radius)
            selection -= selection

        elif shape == 3:
            print("You have chosen Triangle!")
            while True:
                try:
                    side_base = float(input("Please enter base of "
                                            "triangle: "))
                    break
                except ValueError:
                    print("Error, input a valid number.")
            while True:
                try:
                    side2 = float(input("Please enter a side of the "
                                        "triangle: "))
                    break
                except ValueError:
                    print("Error, input a proper value")
            while True:
                try:
                    side3 = float(input("Please enter another side of the "
                                        "triangle: "))
                    break
                except ValueError:
                    print("Error, input a proper value")
            while True:
                try:
                    angle = float(input("Please enter an angle: "))
                    break
                except ValueError:
                    print("Error, choose a valid angle")
            triangle_area_perimeter_height(side_base, side2, side3, angle)
            selection -= selection

        elif shape == 4:
            print("You have chosen Misc!")
            while True:
                try:
                    select = int(input("(1) For name multiplier.\n(2) For"
                                       " " 
                                       "floor "
                                       "division.\n(3) % Modulo operation.\n"))
                    break
                except ValueError:
                    print("Error, not a valid input try again.")
            if select == 1:
                name = input("What is your name? ")
                while True:
                    try:
                        number = int(input("Pick a number between 1-100: "))
                        break
                    except ValueError:
                        print("Error, must be a whole number.")
                misc(name, number)
                selection -= selection
            elif select == 2:
                while True:
                    try:
                        num1 = float(input("Enter a number you would like to "
                                           "check: "))
                        break
                    except ValueError:
                        print("Error, not a number")
                while True:
                    try:
                        num2 = float(input("Enter the number that is "
                                           "checking: "))
                        break
                    except ValueError:
                        print("Error, not a number")
                floor = num1 // num2
                print("Your number is: ", format(floor))
                selection -= selection
            elif select == 3:
                while True:
                    try:
                        num3 = float(input("Enter any number: "))
                        break
                    except ValueError:
                        print("Error, not a valid input try again.")
                while True:
                    try:
                        num4 = float(input("Enter any number: "))
                        break
                    except ValueError:
                        print("Error, not a valid input try again.")
                modulo = num3 % num4
                print("Your number is: ", format(modulo))
                selection -= selection
            else:
                print("Error, try a different input")

        else:  # A code to stop and quit program
            print(
                "Done! Thank you for using my shape calculator.")
            # Add something cool
            frog = "  @..@\n (----)\n( >__< )\n^^ ~~ ^^\n"
            print(frog * 3)
            # To show I can use a string multiplier
            print("Good" + "Bye!", end='')
            done += 1
            # Ends the program


main()
