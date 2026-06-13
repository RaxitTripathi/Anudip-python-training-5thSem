""" 1. Student Information System (Basic) 
Problem Statement: 
Create a Student class to store the student's name, roll number, and marks obtained in three subjects. 
Implement methods to: 
• Accept student details.  
• Calculate the total marks.  
• Calculate the percentage.  
• Display the complete student report.  """


class Student:

    def __init__(self, name, roll_no, subjects):
        self.name = name
        self.roll_no = roll_no
        self.subjects = subjects
        self.total = 0
        self.percentage = 0

    def total_marks(self):
        self.total = 0
        for mark in self.subjects:
            self.total += mark
        return self.total

    def display_percentage(self):
        self.percentage = (self.total / (len(self.subjects) * 100)) * 100
        return self.percentage

    def display_report(self):
        print("\n------ Student Report ------")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Total Marks:", self.total)
        print("Percentage:", self.percentage)


# Main
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = []
for i in range(3):
    mark = float(input(f"Enter marks of subject {i+1}: "))
    subjects.append(mark)

student = Student(name, roll_no, subjects)

student.total_marks()
student.display_percentage()

print("Total Marks:", student.total)
print("Percentage:", student.percentage)

student.display_report()