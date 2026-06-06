'''Question 1: Employee Performance Evaluation 
Problem Statement 
A company stores employee details in a tuple. Each employee record contains: 
employees = ( 
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
) 
Where: 
• First value = Employee ID  
• Second value = Employee Name  
• Third value = Performance Score  
Tasks 
Write a Python program to: 
1. Display details of employees scoring 80 or above.  
2. Count the number of employees who need improvement (score below 60).  
3. Find the employee with the highest score.  
4.Create a list containing the names of all employees scoring above 75.  
5. Display the performance category for each employee:  
o 90 and above → Excellent  
o 75 to 89 → Good  
o 60 to 74 → Average  
o Below 60 → Needs Improvement ''' 

#creating employees data
employees = ( 
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
) 

#  Display details of employees scoring 80 or above.  
print("Employees Scoring 80 or Above: ")
for score in employees:
    if(score[2]>=80):
        print(score[0],score[1],score[2])

#Count the number of employees who need improvement (score below 60)
improve_count=0
for count in employees:
    if(count[2]<60):
        improve_count +=1

print("\nEmployees Needing Improvement: ",count)   


#Find the employee with the highest score.

print("\nHighest performer:")
highest_score=employees[0]
for score in employees:
    if(score[2]>highest_score[2]):
        highest_score=score

print(highest_score[0],highest_score[1],highest_score[2])    

#Create a list containing the names of all employees scoring above 75

high_performance=[]
for i in employees:
    if i[2] > 75:
        high_performance.append(i)

print("\nHigh Performers:")
print(high_performance)


# Display the performance category for each employee
print("\nPerformance Categories:")
for man in employees:
    if(man[2] >= 90):
        print(man[1],"->Excellent")
    elif(man[2] >= 75):
        print(man[1],"->Good")
    elif(man[2] >= 75):
        print(man[1],"->Average")
    else:
        print(man[1],"->Needs Improvement")    