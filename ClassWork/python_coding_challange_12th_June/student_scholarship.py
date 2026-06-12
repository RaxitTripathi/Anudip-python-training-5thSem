""" Problem 2: Student Scholarship Evaluation System 
Problem Statement 
The marks obtained by students in the final examination are stored as follows: 
Sample Data 
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
Tasks 
1. Display students scoring above 85 marks.  
2. Find the topper.  
3. Find the student with the lowest marks.  
4. Calculate class average marks.  
5. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
6. Create a list of scholarship students (marks ≥ 90).  """



#let m=marks

marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

# 1. Students scoring above 85
print("Students above 85:")
for name, m in marks.items():
    if m > 85:
        print(name)

# 2. Topper 
topper_name = ""
topper_marks = -1

for name, m in marks.items():
    if m > topper_marks:
        topper_marks = m
        topper_name = name

print("\nTopper:", topper_name, topper_marks)

# 3. Lowest marks 
lowest_name = ""
lowest_marks = 101 

for name, m in marks.items():
    if m < lowest_marks:
        lowest_marks = m
        lowest_name = name

print("\nLowest:", lowest_name, lowest_marks)

# 4. Class average
total = 0
count = 0

for m in marks.values():
    total += m
    count += 1

average = total / count
print("\nAverage:", average)

# 5. Grades
print("\nGrades:")
for name, m in marks.items():
    if m >= 90:
        grade = "A"
    elif m >= 75:
        grade = "B"
    elif m >= 50:
        grade = "C"
    else:
        grade = "F"

    print(name, "->", grade)

# 6. Scholarship students (>=90)
print("\nScholarship Students:")
for name, m in marks.items():
    if m >= 90:
        print(name)

""" output:

Students above 85:
Anuj
Priya
Sneha
Anjali

Topper: Sneha 95

Lowest: Rohit 47

Average: 76.4

Grades:
Anuj -> A
Rahul -> B
Priya -> B
Neha -> C
Amit -> C
Sneha -> A
Karan -> B
Pooja -> C
Rohit -> F
Anjali -> A

Scholarship Students:
Anuj
Sneha
Anjali """
