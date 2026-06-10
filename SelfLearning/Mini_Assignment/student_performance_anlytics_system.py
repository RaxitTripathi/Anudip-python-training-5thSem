""" 1. Student Performance Analytics System 
Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary. 
Example Structure 
students = { 
    "S101": {"name": "Anuj", "marks": 85}, 
    "S102": {"name": "Rahul", "marks": 72} 
} 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85).  
Expected Learning 
• Nested Dictionaries  
• Dictionary Traversal  
• Searching  
• Aggregation  
• Report Generation  """


from student_performence_operation import *


# empty dictionary to store students
students = {}

# 1. Input 30 students
print("Enter details of 30 students:\n")

for i in range(30):
    print(f"\nStudent {i+1}")

    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students[sid] = {
        "name": name,
        "marks": marks
    }

print("\nAll 30 students added successfully!\n")


# 2. Menu system
while True:

    print("\n----- STUDENT MENU -----")
    print("1. Display all students")
    print("2. Search student")
    print("3. Add student")
    print("4. Update marks")
    print("5. Delete student")
    print("6. Topper & Lowest")
    print("7. Class average")
    print("8. Pass/Fail count")
    print("9. Grade report")
    print("10. Above average students")
    print("11. Scholarship students")
    print("12. Exit")

    choice = input("Enter choice: ")

    # 1. Display all
    if choice == "1":
        display_all_students(students)

    # 2. Search
    elif choice == "2":
        sid = input("Enter Student ID: ")
        search_student(sid, students)

    # 3. Add
    elif choice == "3":
        sid = input("Enter Student ID: ")
        new_student(sid, students)

    # 4. Update marks
    elif choice == "4":
        sid = input("Enter Student ID: ")
        update_marks(sid, students)

    # 5. Delete
    elif choice == "5":
        sid = input("Enter Student ID: ")
        delete_students(sid, students)

    # 6. Topper & Lowest
    elif choice == "6":
        position_students(students)

    # 7. Average
    elif choice == "7":
        average_class(students)

    # 8. Pass/Fail
    elif choice == "8":
        count_students(students)

    # 9. Grades
    elif choice == "9":
        grade_students(students)

    # 10. Above average
    elif choice == "10":
        above_average(students)

    # 11. Scholarship
    elif choice == "11":
        scholarship_student(students)

    # 12. Exit
    elif choice == "12":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")