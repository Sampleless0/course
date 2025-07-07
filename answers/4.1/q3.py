# uses math function
import math

# function to print menu
def display_menu():
    print("")
    print('Geometry calculator menu')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')
    print("")

# function to calculate area of circle (takes in radius)
def area_circle(radius):
    return math.pi * radius ** 2

# function to calculate circumference of circle (takes in radius)
def circle_circumference(radius):
    return 2 * math.pi * radius

# function to calculate area of rectangle (takes in length and width)
def area_rectangle(length, width):
    return length * width

# function to calculate perimeter of rectangle (takes in length and width)
def perimeter_rectangle(length, width):
    return 2 * (length + width)

# function for main code
def main():
    choice = 0

    # while loop that lets users repeat the calculations until they quit
    while choice != 5:
        display_menu()

        # tries to receive choice as int
        try:
            choice = int(input('Enter your choice: '))
        except Exception:
            print("invalid input")
            break

        # ifelse statements to calculate results
        if choice == 1:
            radius = float(input("Enter the circle's radius: "))
            print(f'\nThe area of the circle = {area_circle(radius)}')
        elif choice == 2:
            radius = float(input("Enter the circle's radius: "))
            print(f'\nThe circumference of the circle = {circle_circumference(radius)}')
        elif choice == 3:
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            print(f'\nThe area of the rectangle = {area_rectangle(length, width)}')
        elif choice == 4:
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            print(f'\nThe perimeter of the rectangle = {perimeter_rectangle(length, width)}')
        elif choice == 5:
            print('Exiting the program. . .')
            main()
        else:
            print('Error: invalid selection.')
            break

# run main function
main()
