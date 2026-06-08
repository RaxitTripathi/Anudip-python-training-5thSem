'''Problem Statement: Student Record Management Using Tuples 
A coaching institute wants to store student information in a way that prevents accidental modification of 
records. 
Each student's record should contain: 
• Student ID  
• Student Name  
• Course Name  
• Fees Paid  
Store the details of 5 students using tuples and perform the following operations: 
1. Display all student records.  
2. Display the first student's details.  
3. Display the last student's details using negative indexing.  
4. Display only Student ID and Name for all students.  
5. Count the total number of students.  
6. Check whether a student named "Rahul" exists in the records.  
Sample Data 
students = ( 
    (101, "Rahul", "Python", 25000), 
    (102, "Priya", "Java", 30000), 
    (103, "Amit", "Data Science", 45000), 
    (104, "Sneha", "Python", 25000), 
    (105, "Rohan", "MERN", 40000) 
) '''

# Student records stored in tuples

students = (
    (101, "Rahul", "Python", 25000),
    (102, "Priya", "Java", 30000),
    (103, "Amit", "Data Science", 45000),
    (104, "Sneha", "Python", 25000),
    (105, "Rohan", "MERN", 40000)
)

# 1. Display all student records
print("All Student Records:")
for student in students:
    print(student)

# 2. Display first student's details
print("\nFirst Student Details:")
print(students[0])

# 3. Display last student's details using negative indexing
print("\nLast Student Details:")
print(students[-1])

# 4. Display only Student ID and Name for all students
print("\nStudent ID and Name:")
for student in students:
    print("ID:", student[0], "Name:", student[1])

# 5. Count total number of students
print("\nTotal Number of Students:", len(students))

# 6. Check whether a student named 'Rahul' exists
found = False

for student in students:
    if student[1] == "Rahul":
        found = True
        break

if found:
    print("\nRahul exists in the records.")
else:
    print("\nRahul does not exist in the records.")