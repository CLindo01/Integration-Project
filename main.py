#Christian Lindo
#Shape Calclulator
# Hello this program will ask for what shape you'd like to calculate
import math
# Used in order to run math.pi

def circle_diameter_circumference_area(radius):
    circumference = 2 * (math.pi * radius)
    diameter = radius * 2
    area = math.pi * (radius**2)
    print("Your circle's dimensions are as followed:","\nCircumference:", format(circumference, '.2f'),"\nRadius:", format(radius, '.2f'),"\nDiameter:", format(diameter, '.2f'),"\nArea:", format(area, '.2f'))

def square_area_perimeter(side_l, side_w):
    area = side_l * side_w
    perimeter = (side_l*2)+(side_w*2)
    print("Your area is:", format(area, '.2f'),"\nYour perimeter is:",format(perimeter, '.2f'))

def triangle_area_perimeter_height(side1, side2, side3, angle):
    area = (side1*side2)*(math.sin(angle)/2)
    height = 2*(area/side1)
    perimeter = side1+side2+side3
    print("Your area is:", format(area, '.2f'),"\nYour height is:", format(height, '.2f',),"\nYour perimeter is:",format(perimeter, '.2f'))

def misc(name, number):
    if not number <= 100 and number >= 1:  # Using "not" and "and" in order to run a test to make sure value matches as asked in the prompt.
        print("Invalid number, try again!")
        number = int(input("Pick a number between 1-100: ")) #
    for x in range(0, number):
        print(name, sep='', )

def main():
    selection = 0
    done = 0
    print("Hello user and welcome to my shape calculator program!")
    print("Use the program as much as you like! When you are finished, input (5.) to quit")
    while done != 1:
        while selection <=4:
            if selection == 0:
                print("1. Square")
                selection +=1
            elif selection == 1:
                    print("2. Circle")
                    selection += 1
            elif selection == 2:
                print("3. Triangle")
                selection +=1
            elif selection == 3:
                print("4. Misc")
                selection +=1
            else:
                print("5. Done")
                selection+=1

        shape = int(input("What shape would you like to calculate?\nPick a number from the following choices: "))
        # asks what calculation it would like to run
        if shape > 5 or shape < 1:
            print("Invalid, Try Again")
            shape = int(input("What shape would you like to calculate?\nPick a number from the following choices: "))
        elif shape == 1:
            print("You have chosen Square!")
            side1 = float(input("Input Side Length: "))
            side2 = float(input("Input side Width: ")) # ask for input of numbers
            square_area_perimeter(side1, side2) #define statement for output
            selection-=selection
            #Resets list choices and reruns input selection
            # output calculation requested and restarts program
        elif shape ==2:
            print("You have chosen Circle!")
            radius = float(input("Please enter the radius of the circle: "))
            circle_diameter_circumference_area(radius)
            selection-=selection

        elif shape == 3:
            print("You have chosen Triangle!")
            side_base = float(input("Please enter base of triangle: "))
            side2 = float(input("Please enter a side of the triangle: "))
            side3 = float(input("Please enter another side of the triangle: "))
            angle = float(input("Please enter an angle: "))
            triangle_area_perimeter_height(side_base, side2, side3, angle)
            selection -= selection

        elif shape == 4:
            print("You have chosen Misc!")
            name = input("What is your name? ")
            number = int(input("Pick a number between 1-100: "))
            misc(name,number)
            selection -= selection

        elif shape == 5: #A code to stop and quit program
            print("Done! Thank you for using my shape calculator.")  # Add something cool
            print("Good" + "Bye!", end='')
            done+=1
            # Ends the program
main()
