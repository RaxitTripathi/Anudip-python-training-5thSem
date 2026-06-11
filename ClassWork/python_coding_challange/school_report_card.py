# Problem 4: School Report Card Generator 
# Problem Statement 
# Student marks are stored in marks.txt. 
# Sample Input/Data (marks.txt) 
# S101,Anuj,92 
# S102,Rahul,76 
# S103,Priya,88 
# S104,Neha,45 
# S105,Amit,58 
# S106,Sneha,95 
# S107,Karan,81 
# S108,Pooja,73 
# S109,Rohit,39 
# S110,Anjali,90 
# Tasks 
# 1. Calculate grades for all students.  
# Passed Students: 9 
# Failed Students: 1 
# 2. Generate a report card file report_card.txt.  
# 3. Display topper details.  
# 4. Count pass and fail students.  
# 5. Display students eligible for merit certificates (marks ≥ 90). 

# Problem 4: School Report Card Generator

# Read data from marks.txt

file = open("marks.txt", "r")
students = file.readlines()
file.close()

# Variables
pass_count = 0
fail_count = 0
topper_name = ""
topper_marks = 0
merit_students = []

# Create report card file
report = open("report_card.txt", "w")

print("REPORT CARD")
print("-" * 40)

for student in students:
    student = student.strip()

    emp_id, name, marks = student.split(",")
    marks = int(marks)

    # Calculate grade
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    # Pass/Fail Count
    if marks >= 50:
        status = "PASS"
        pass_count += 1
    else:
        status = "FAIL"
        fail_count += 1

    # Topper
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name
        topper_id = emp_id

    # Merit Certificate
    if marks >= 90:
        merit_students.append(name)

    # Display Student Report
    print(emp_id, name, marks, grade, status)

    # Write to report_card.txt
    report.write(
        emp_id + "," +
        name + "," +
        str(marks) + "," +
        grade + "," +
        status + "\n"
    )

report.close()

# Display Topper
print("\nTopper Details")
print("ID:", topper_id)
print("Name:", topper_name)
print("Marks:", topper_marks)

# Pass and Fail Count
print("\nPassed Students:", pass_count)
print("Failed Students:", fail_count)

# Merit Certificate Students
print("\nStudents Eligible for Merit Certificate:")
for student in merit_students:
    print(student)