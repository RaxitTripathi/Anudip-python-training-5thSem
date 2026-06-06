'''Wap that contain the record of 10 employee Employee id use as key and salry as value 
-find out the total no of employee having salary greater than 30 thousand 
-display the list of employees whose salary is below 20 thousand'''

employee_dict={}
employee_total=10
while(employee_total):
    employee_id=input("Enter id:")
    employee_salary=int(input("Enter salary:"))
    if(employee_salary <= 0):
        print("Employee salary can not be in negative retype id and salary")
        continue

    employee_dict[employee_id] = employee_salary
    employee_total -= 1
# find out the total no of employee having salary greater than 30 thousand   

count_employee=0
for employee in employee_dict:
    if(employee_dict[employee] > 30000):
        count_employee += 1

print("Total no of employee having salary greater than 30 thousand",count_employee)


# display the list of employees whose salary is below 20 thousand
print("Employees having salary below 20000:")
employee_list=[]
for employee in employee_dict:
    if(employee_dict[employee] < 20000):
        employee_list.append(employee)
print(employee_list)