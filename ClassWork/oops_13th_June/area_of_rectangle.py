#Operation On rectangle

class Rectangle:
#defining a constructor
    def __init__(self,length,breadth):
        self.length =length
        self.breadth =breadth
#Method for display area
    def display_area(self):
        print("Area of Rectangle:",self.length *self.breadth)   
#Method for display Parameter
    def display_parameter(self):
        print("Paremeter of Rectangle:",2*(self.length + self.breadth)) 

#Main
length=float(input("Enter Length of Rectangle:"))
    #Validation    
if length <= 0:
    exit("Length must be greater than 0")

breadth=float(input("Enter Breadth of Rectangle:"))
    #Validation    
if breadth <= 0:
    exit("Breadth must be greater than 0") 

rectangle=Rectangle(length,breadth)

while(True):     
    print("""---------Choose Operation------------
1->Area of Rectangle
2->Paremeter of Rectangle
3->Exit""")
        
    user=int(input("Enter choice:"))
    if user == 1:
        rectangle.display_area()
    elif user ==2:
        rectangle.display_parameter()
    elif user ==3:
        print("All operation Done:")
        break
    else:
        print("Invalid Input:")

    another_operation=input("Do you want to perform another operation? (yes/no): ")
    if another_operation.lower()!="yes":
        print("Thank you for using our services!")
        break
    print("\n----------------------------------")        
