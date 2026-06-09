# Creates a python program to user which provide 2d figure circle rectangle and square after selecting the figure the user again ask type of corresponding data from the figure after input of corresponding data again provide a menu to select the operation area,perimeterand as per the data provided by user or operation selected by user display the result of operation. This task will be repeated again and again until user select option to exit from that figure. 

from shapes_2d import *

while(True):
    user_input=int(input(('''Select operation based on option:
    1->Rectangle
    2->Square
    3->Circle
    4->Exit:''')))

#Rectangle
    if user_input ==1:
        length=float(input("\nEnter Length of rectangle:"))

        #validation
        if length <=0:
            exit("\nLength of rectangle can not be 0 or less")

        breadth=float(input("Enter Breadth od rectangle:")) 
        #validation
        if breadth <=0:
            exit("Breadth of rectangle can not be 0 or less")   
        print("\nArea of rectangle is:",area_of_rectangle(length,breadth))
        print("Parameter of rectangle is:",parameter_of_rectangle(length,breadth))

#Square
    elif user_input ==2:
        side=float(input("\nEnter side of square:"))
        
        #Validation
        if side <=0:
            exit("Side of square can't be zero")

        print("\nArea of square is:",area_of_square(side))
        print("Parameter of square is:",parameter_of_square(side))

#Circle
    elif user_input ==3:
        radius=float(input("\nEnter radius of circle:"))
        
        #Validation
        if radius <=0:
            exit("radius of circle can't be zero")

        print("\nArea of circle is:",area_of_circle(radius))
        print("Circumferance of circle is:",circumference_of_circle(radius))

#Exit
    elif user_input ==4:
        print("\nExit from Operations:")
        break

#Invalid input
    else:
        print("\nInvalid input")    

            


        
