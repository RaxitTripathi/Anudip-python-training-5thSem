# Problem Statement 
# A teacher has marks of students stored in a list. 
# marks = [78, 45, 92, 35, 88, 40, 99, 56] 
# Write a program to: 
# 1. Display all passed students (marks ≥ 40).  
# 2. Count the number of failed students.  
# 3. Find the highest and lowest marks without using max() or min().  
# 4. Create a new list containing marks above 75.  


marks = [78, 45, 92, 35, 88, 40, 99, 56] 

highest_marks=marks[0]
lowest_marks=marks[0]

passed_student=[]
fail_count=0
merit_list=[]


for i in marks:
    if(i >= 40):
        passed_student.append(i)
    
    if(i<40):
        fail_count+=1
    
    if(i > 75):
        merit_list.append(i)

    if(i > highest_marks):
        highest_marks=i
    elif(i < lowest_marks):
        lowest_marks=i   

print("Passed Students:",passed_student)
print("Failed Count:",fail_count)
print("Highest marks:",highest_marks)
print("Lowest marks:",lowest_marks)
print("Merit List:",merit_list)