""" 4. Employee Salary Management (Intermediate) 
Problem Statement: 
Create an Employee class containing employee ID, name, and monthly salary. 
Implement methods to: 
• Display employee details.  
• Calculate annual salary.  
• Increase salary by a given percentage.  
Sample Output: 
Employee Name : Rohan 
Monthly Salary: ₹50000 
Annual Salary : ₹600000 
Updated Salary: ₹55000 """


class Employee:

    def __init__(self,emp_id,name,monthly_salary):
        self.emp_id =emp_id
        self.name =name
        self.monthly_salary =monthly_salary
        self.annual=1
        self.updated=0

    def annual_salary(self):
        self.annual = self.monthly_salary *12
        return self.annual
    
    def updated_salary(self,increment): 
        self.updated = self.monthly_salary * increment / 100
        print("Updated Salary:",self.updated +self.monthly_salary)
        self.monthly_salary += self.updated

    def employee_detail(self):
        print("Employee Name :",self.name) 
        print("Employee Id :",self.emp_id)    
        print("Monthly Salary :",self.monthly_salary)
        print("Annual Salary :",self.annual_salary())


emp_id=(input("Enter Id:"))
if emp_id.isspace():
    exit("Employee Id does not need to contain Space:")
name=input("Enter Employee name:")
#Validation
if name.isdigit():
    exit("Name does not contain digits:")  

monthly_salary=float(input("Enter salary:"))

employee=Employee(emp_id,name,monthly_salary)

increment=float(input("Enter increment in monthly salary: "))
if increment <= 0 and increment >100:
    exit("Invalid Increment %")

employee.updated_salary(increment)
employee.employee_detail()    