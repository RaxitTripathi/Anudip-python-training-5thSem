#Methods of Rectangle

def area_of_rectangle(length,breadth):
    area=length*breadth
    return area

def parameter_of_rectangle(length,breadth):
    parameter=2*(length + breadth)
    return parameter


#Methods of square

def area_of_square(side):
    area=side*side
    return area

def parameter_of_square(side):
    parameter=4*side
    return parameter 

#Methods for circle

def area_of_circle(radius):
    area=3.14*radius*radius
    return area

def circumference_of_circle(radius):
    parameter=2*3.14*radius
    return parameter    

#Method for triangle

def area_of_triangle(base, height):
    return 0.5 * base * height

def perimeter_of_triangle(a, b, c):
    return a + b + c