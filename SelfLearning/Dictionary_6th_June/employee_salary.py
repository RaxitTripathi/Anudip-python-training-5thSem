""" 3. Employee Salary Processing 
Sample Data 
salary = { 
    "EMP101": 45000, 
    "EMP102": 62000, 
    "EMP103": 38000, 
    "EMP104": 75000, 
    "EMP105": 54000, 
    "EMP106": 29000, 
    "EMP107": 82000, 
    "EMP108": 48000, 
    "EMP109": 36000, 
    "EMP110": 68000 
} 
Tasks 
• Display employees earning above ₹60,000.  
• Count employees earning below ₹40,000.  
• Find the highest-paid employee.  
• Create a list of employees eligible for a bonus (salary > ₹50,000).  
• Calculate the average salary.  """


salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Employees earning above ₹60,000
print("Employees earning above ₹60,000:")
for emp_id, sal in salary.items():
    if sal > 60000:
        print(emp_id, ":", sal)

# Count employees earning below ₹40,000
count = 0
for sal in salary.values():
    if sal < 40000:
        count += 1
print("\nEmployees earning below ₹40,000:", count)

# Highest-paid employee
highest_paid = max(salary, key=salary.get)
print("\nHighest-paid employee:", highest_paid)
print("Salary:", salary[highest_paid])

# Employees eligible for bonus (salary > ₹50,000)
bonus_list = []
for emp_id, sal in salary.items():
    if sal > 50000:
        bonus_list.append(emp_id)

print("\nEmployees eligible for bonus:")
print(bonus_list)

# Average salary
total_salary = 0

for sal in salary.values():
    total_salary += sal

average_salary = total_salary / len(salary)

print("\nAverage Salary:", average_salary)