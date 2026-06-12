""" 12. Employee Salary Report Generator 
Problem Statement 
A company stores employee details in a text file named employees.txt. 
File Format 
EMP101,Anuj,45000 
EMP102,Rahul,52000 
EMP103,Priya,38000 
EMP104,Neha,61000 
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP106,Karan,46000 
EMP108,Pooja,62000 
EMP109,Rohit,33000 
EMP110,Anjali,68000 
Requirements 
Create a menu-driven program to: 
1. Display all employee records.  
2. Search employee details using Employee ID.  
3. Calculate the average salary.  
4. Find the highest-paid and lowest-paid employee.  
5. Display employees earning above ₹50,000.   
6. Generate salary categories:  
o High (₹60,000 and above)  
o Medium (₹40,000–₹59,999)  
o Low (Below ₹40,000)  """



# Employee Payroll Management System

while True:
    print("\n===== EMPLOYEE PAYROLL MANAGEMENT SYSTEM =====")
    print("1. Display all employee records")
    print("2. Search employee by ID")
    print("3. Calculate average salary")
    print("4. Highest-paid and Lowest-paid employee")
    print("5. Employees earning above ₹50000")
    print("6. Salary Categories")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Display all records
    if choice == "1":
        file = open("employees.txt", "r")
        data = file.read()
        file.close()

        print("\nEmployee Records:")
        print(data)

    # Search employee by ID
    elif choice == "2":
        emp_id = input("Enter Employee ID: ")

        file = open("employees.txt", "r")
        data = file.read()
        file.close()

        records = data.split("\n")
        found = False

        for record in records:
            details = record.split(",")

            if len(details) == 3 and details[0] == emp_id:
                print("\nEmployee Found")
                print("ID:", details[0])
                print("Name:", details[1])
                print("Salary:", details[2])
                found = True
                break

        if not found:
            print("Employee not found")

    # Average salary
    elif choice == "3":
        file = open("employees.txt", "r")
        data = file.read()
        file.close()

        records = data.split("\n")

        total_salary = 0
        count = 0

        for record in records:
            details = record.split(",")

            if len(details) == 3:
                total_salary += int(details[2])
                count += 1

        if count > 0:
            print("Average Salary =", total_salary / count)

    # Highest-paid and Lowest-paid employee
    elif choice == "4":
        file = open("employees.txt", "r")
        data = file.read()
        file.close()

        records = data.split("\n")

        highest_name = ""
        highest_salary = 0

        lowest_name = ""
        lowest_salary = 999999999

        for record in records:
            details = record.split(",")

            if len(details) == 3:
                salary = int(details[2])

                if salary > highest_salary:
                    highest_salary = salary
                    highest_name = details[1]

                if salary < lowest_salary:
                    lowest_salary = salary
                    lowest_name = details[1]

        print("\nHighest Paid Employee:")
        print(highest_name, "-", highest_salary)

        print("\nLowest Paid Employee:")
        print(lowest_name, "-", lowest_salary)

    # Employees earning above 50000
    elif choice == "5":
        file = open("employees.txt", "r")
        data = file.read()
        file.close()

        records = data.split("\n")

        print("\nEmployees earning above ₹50000:")

        for record in records:
            details = record.split(",")

            if len(details) == 3 and int(details[2]) > 50000:
                print(details[0], details[1], details[2])

    # Salary categories
    elif choice == "6":
        file = open("employees.txt", "r")
        data = file.read()
        file.close()

        records = data.split("\n")

        print("\nHIGH CATEGORY (₹60000 and above)")
        for record in records:
            details = record.split(",")
            if len(details) == 3 and int(details[2]) >= 60000:
                print(details[1], "-", details[2])

        print("\nMEDIUM CATEGORY (₹40000 - ₹59999)")
        for record in records:
            details = record.split(",")
            if len(details) == 3 and 40000 <= int(details[2]) < 60000:
                print(details[1], "-", details[2])

        print("\nLOW CATEGORY (Below ₹40000)")
        for record in records:
            details = record.split(",")
            if len(details) == 3 and int(details[2]) < 40000:
                print(details[1], "-", details[2])

    # Exit
    elif choice == "8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
    