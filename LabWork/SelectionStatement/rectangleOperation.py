#Wap to calculate area and parameter of a rectangle 

print("----- Rectangle -----")
#----------------Length-----------------------
length = float(input("Enter length (cm): "))
#----------------Breadth-----------------------
breadth = float(input("Enter breadth (cm): "))

#------------------Inputs------------------------
print("Length=",length)
print("Breadth=",breadth)
#----------------Validation---------------------
if length <= 0 or breadth <= 0:
    exit("Length and breadth must be > 0")
#----------Area and parimeter--------------
area = length * breadth
perimeter = 2 * (length + breadth)

print(f"Area = {area:.2f} cm²")
print(f"Perimeter = {perimeter:.2f} cm")