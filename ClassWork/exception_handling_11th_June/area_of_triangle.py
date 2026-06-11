""" Problem Statement: Area of a Triangle Using Three Sides with Exception Handling 
Design a Python program to calculate the area of a triangle using Heron's Formula. The program should 
accept the lengths of the three sides of the triangle from the user and display the calculated area. 
However, the program must handle the following exceptional situations gracefully: 
1. If the user enters a non-numeric value instead of a number for any side, display an appropriate error 
message.  
2. If any of the entered side lengths are zero or negative, inform the user that triangle sides must be 
greater than zero.  
3. If the three entered side lengths cannot form a valid triangle according to the Triangle Inequality 
Theorem, notify the user that the triangle is invalid.  
4. Ensure that the program does not terminate abruptly due to invalid input and provides meaningful 
feedback using exception handling.  
5. Display a message indicating that the triangle area calculation process has been completed, 
regardless of whether the calculation was successful or an exception occurred.  
Note: Use Heron's Formula to calculate the area of the triangle: 
�
�=𝑎+𝑏+𝑐)/2
2 
Area=√𝑠(𝑠−𝑎)(𝑠−𝑏)(𝑠−𝑐) 
 
Sample Scenario: 
A construction engineer is using an application to estimate the amount of material required for a triangular 
plot of land. Incorrect measurements or invalid data entry should not cause the application to crash; 
instead, it should guide the user by displaying appropriate error messages and allowing them to understand 
the issue with the provided inputs """

try:
    side1 = float(input("Enter first side: "))
    if side1 <= 0:
        raise Exception("First side must be greater than zero.")

    side2 = float(input("Enter second side: "))
    if side2 <= 0:
        raise Exception("Second side must be greater than zero.")

    side3 = float(input("Enter third side: "))
    if side3 <= 0:
        raise Exception("Third side must be greater than zero.")

    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise Exception("The given sides cannot form a valid triangle.")

    s = (side1 + side2 + side3) / 2

    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

    print("Area of Triangle =", area)

except ValueError:
    print("Error: Please enter numeric values only.")

except Exception as e:
    print("Error:", e)

finally:
    print("Triangle area calculation process completed.")