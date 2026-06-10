""" 3. Student Result Processing System 
Problem Statement 
Student marks are stored in results.txt. 
File Format 
S101,Anuj,85 
S102,Rahul,72 
S103,Priya,96 
S104,Neha,68 
S105,Amit,39 
S106,Sneha,54 
S107,Karan,91 
S108,Pooja,78 
S109,Rohit,47 
S110,Anjali,88 
Requirements 
Write a program to: 
1. Display all student records.  
2. Search a student using Student ID.  
3. Find topper and lowest scorer.  
4. Calculate class average.  
5. Count pass and fail students.  
6. Generate grades:  
o A (90+)  
o B (75–89)  
o C (40–74)  
o F (<40)  
7. Write grade reports into a new file named grades.txt.  """

# Student Result Processing System


# Display all student records
def display_records():

    file = open("results.txt", "r")
    data = file.read()
    file.close()

    print("\n--- Student Records ---")
    print(data)


# Search student using Student ID
def search_student():

    student_id = input("Enter Student ID: ")

    file = open("results.txt", "r")
    data = file.read()
    file.close()

    students = data.split("\n")

    found = False

    for student in students:

        details = student.split(",")

        if details[0] == student_id:

            print("\nStudent Found")
            print("ID    :", details[0])
            print("Name  :", details[1])
            print("Marks :", details[2])

            found = True
            break

    if not found:
        print("Student not found")


# Find topper and lowest scorer
def topper_and_lowest():

    file = open("results.txt", "r")
    data = file.read()
    file.close()

    students = data.split("\n")

    topper_name = ""
    topper_marks = -1

    lowest_name = ""
    lowest_marks = 101

    for student in students:

        details = student.split(",")

        marks = int(details[2])

        if marks > topper_marks:
            topper_marks = marks
            topper_name = details[1]

        if marks < lowest_marks:
            lowest_marks = marks
            lowest_name = details[1]

    print("\nTopper :", topper_name, "-", topper_marks)
    print("Lowest Scorer :", lowest_name, "-", lowest_marks)


# Calculate class average
def class_average():

    file = open("results.txt", "r")
    data = file.read()
    file.close()

    students = data.split("\n")

    total = 0

    for student in students:

        details = student.split(",")

        total += int(details[2])

    average = total / len(students)

    print("\nClass Average =", round(average, 2))


# Count pass and fail students
def pass_fail_count():

    file = open("results.txt", "r")
    data = file.read()
    file.close()

    students = data.split("\n")

    passed = 0
    failed = 0

    for student in students:

        details = student.split(",")

        marks = int(details[2])

        if marks >= 40:
            passed += 1
        else:
            failed += 1

    print("\nPassed Students :", passed)
    print("Failed Students :", failed)


# Generate grades and write report to grades.txt
def generate_grades():

    file = open("results.txt", "r")
    data = file.read()
    file.close()

    students = data.split("\n")

    report = ""

    for student in students:

        details = student.split(",")

        student_id = details[0]
        name = details[1]
        marks = int(details[2])

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        report += student_id + "," + name + "," + str(marks) + "," + grade + "\n"

    file = open("grades.txt", "w")
    file.write(report)
    file.close()

    print("\nGrade report generated successfully")


# Display menu and perform selected operation
while True:

    print("\n===== Student Result Processing System =====")
    print("1. Display All Records")
    print("2. Search Student")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grade Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_records()

    elif choice == "2":
        search_student()

    elif choice == "3":
        topper_and_lowest()

    elif choice == "4":
        class_average()

    elif choice == "5":
        pass_fail_count()

    elif choice == "6":
        generate_grades()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")