# Creates a python program to user which provide 2d figure circle rectangle and square after selecting the figure the user again ask type of corresponding data from the figure after input of corresponding data again provide a menu to select the operation area,perimeterand as per the data provided by user or operation selected by user display the result of operation. This task will be repeated again and again until user select option to exit from that figure. 

# Import all functions from shapes_2d.py
from shapes_2d import *

# Main menu loop
while True:

    user_input = int(input('''
Select operation based on option:
1 -> Rectangle
2 -> Square
3 -> Circle
4 -> Exit

Enter choice: '''))

    # ----------------------- RECTANGLE -----------------------------------
    if user_input == 1:

        length = float(input("\nEnter Length of Rectangle: "))

        # Validation
        if length <= 0:
            print("Length of rectangle cannot be 0 or less.")
            continue

        breadth = float(input("Enter Breadth of Rectangle: "))

        # Validation
        if breadth <= 0:
            print("Breadth of rectangle cannot be 0 or less.")
            continue

        # Rectangle operation menu
        while True:

            user_input_op = int(input('''
Select Operation:
1. Area
2. Perimeter
3. Change Figure

Enter choice: '''))

            if user_input_op == 1:
                print("\nArea of Rectangle =", area_of_rectangle(length, breadth))

            elif user_input_op == 2:
                print("\nPerimeter of Rectangle =", parameter_of_rectangle(length, breadth))

            elif user_input_op == 3:
                break

            else:
                print("Invalid Operation")
                continue

            user = input(
                "\nDo you want to perform another operation on the same figure? (Y/N): "
            ).upper()

            if user == "Y":
                continue

            elif user == "N":
                break

            else:
                print("Invalid Input")
                break

    # ---------------------- SQUARE -------------------------------------
    elif user_input == 2:

        side = float(input("\nEnter Side of Square: "))

        # Validation
        if side <= 0:
            print("Side of square cannot be 0 or less.")
            continue

        # Square operation menu
        while True:

            user_input_op = int(input('''
Select Operation:
1. Area
2. Perimeter
3. Change Figure

Enter choice: '''))

            if user_input_op == 1:
                print("\nArea of Square =", area_of_square(side))

            elif user_input_op == 2:
                print("\nPerimeter of Square =", parameter_of_square(side))

            elif user_input_op == 3:
                break

            else:
                print("Invalid Operation")
                continue

            user = input(
                "\nDo you want to perform another operation on the same figure? (Y/N): "
            ).upper()

            if user == "Y":
                continue

            elif user == "N":
                break

            else:
                print("Invalid Input")
                break

    # ----------------------------- CIRCLE -----------------------------------
    elif user_input == 3:

        radius = float(input("\nEnter Radius of Circle: "))

        # Validation
        if radius <= 0:
            print("Radius of circle cannot be 0 or less.")
            continue

        # Circle operation menu
        while True:

            user_input_op = int(input('''
Select Operation:
1. Area
2. Circumference
3. Change Figure

Enter choice: '''))

            if user_input_op == 1:
                print("\nArea of Circle =", area_of_circle(radius))

            elif user_input_op == 2:
                print("\nCircumference of Circle =", circumference_of_circle(radius))

            elif user_input_op == 3:
                break

            else:
                print("Invalid Operation")
                continue

            user = input(
                "\nDo you want to perform another operation on the same figure? (Y/N): "
            ).upper()

            if user == "Y":
                continue

            elif user == "N":
                break

            else:
                print("Invalid Input")
                break

    # ----------------- EXIT -----------------------
    elif user_input == 4:
        print("\nExiting Program...")
        break

    # ------------------- INVALID CHOICE ------------------------
    else:
        print("\nInvalid Choice")
            


        
