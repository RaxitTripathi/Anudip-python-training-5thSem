from shapes_2d import *

while True:
    print("\n===== Shape Calculator =====")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        if length <= 0 or breadth <= 0:
            print("Length and breadth must be greater than 0.")
        else:
            print("Area =", area_of_rectangle(length, breadth))
            print("Perimeter =", parameter_of_rectangle(length, breadth))

    elif choice == "2":
        side = float(input("Enter side: "))

        if side <= 0:
            print("Side must be greater than 0.")
        else:
            print("Area =", area_of_square(side))
            print("Perimeter =", parameter_of_square(side))

    elif choice == "3":
        radius = float(input("Enter radius: "))

        if radius <= 0:
            print("Radius must be greater than 0.")
        else:
            print("Area =", round(area_of_circle(radius), 2))
            print("Circumference =", round(circumference_of_circle(radius), 2))

    elif choice == "4":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        a = float(input("Enter side 1: "))
        b = float(input("Enter side 2: "))
        c = float(input("Enter side 3: "))

        if base <= 0 or height <= 0 or a <= 0 or b <= 0 or c <= 0:
            print("All values must be greater than 0.")
        else:
            print("Area =", area_of_triangle(base, height))
            print("Perimeter =", perimeter_of_triangle(a, b, c))

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")