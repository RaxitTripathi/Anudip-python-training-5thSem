'''Problem Statement 
Employee data is stored as tuples: 
employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 
Write a program to: 
• Display employees earning above ₹50,000.  
• Find the highest-paid employee.  
• Calculate total salary expenditure.  
• Count employees earning below ₹40,000. '''

employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 

# Display employees earning above ₹50,000.
print("Employees earning above ₹50,000:")
for employee in employees:
    if(employee[1] > 50000):
        print(employee[0],employee[1])

# Find the highest-paid employee.   
print("\nHighest paid employee:")   
highest_paid=employees[0]
for employee in employees:
    if(employee[1] > highest_paid[1]):
        highest_paid=employee
print(highest_paid[0],highest_paid[1])

# Calculate total salary expenditure.

total_salary=0
for employee in employees:
    total_salary += employee[1]

print("\nTotal salary expenditure:",total_salary)


# Count employees earning below ₹40,000    

print("\nEmployees earning below ₹40,000:")
for employee in employees:
    if employee[1] < 40000:
        print(employee[0],employee[1])