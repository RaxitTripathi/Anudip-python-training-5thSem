""" 
1. Student Marks Analysis 
Sample Data 
marks = { 
    "Aarav": 78, 
    "Diya": 92, 
    "Rohan": 45, 
    "Ishita": 88, 
    "Kabir": 56, 
    "Meera": 39, 
    "Arjun": 95, 
    "Saanvi": 67, 
    "Vivaan": 82, 
    "Anaya": 51 
} 
Tasks 
• Display students scoring 80 or above.  
• Count the number of students who failed (marks < 40).  
• Find the highest scorer.  
• Create a list of students scoring between 60 and 75.  
• Assign grades:  
o A: ≥ 90  
o B: 75–89  
o C: 50–74  
o F: < 50 """


marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# 1. Display students scoring 80 or above
print("Students scoring 80 or above:")
for student, score in marks.items():
    if score >= 80:
        print(student, ":", score)

# 2. Count students who failed (marks < 40)
failed_count = 0
for score in marks.values():
    if score < 40:
        failed_count += 1

print("\nNumber of failed students:", failed_count)

# 3. Find the highest scorer

highest_scorer = None
highest_marks = 0

for student in marks:
    if marks[student] > highest_marks:
        highest_marks = marks[student]
        highest_scorer = student

print("\nHighest Scorer:")
print(highest_scorer, ":", highest_marks)

# 4. List students scoring between 60 and 75
students_60_75 = []

for student, score in marks.items():
    if 60 <= score <= 75:
        students_60_75.append(student)

print("\nStudents scoring between 60 and 75:")
print(students_60_75)

# 5. Assign grades
print("\nGrades:")
for student, score in marks.items():

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(student, ":", grade)