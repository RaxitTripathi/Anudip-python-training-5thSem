""" Problem 9: University Course Enrollment Management System 
Problem Statement 
Student enrollment data for university courses is stored below. 
Sample Data 
enrollment = { 
    "Python": 45, 
    "Java": 38, 
    "Data Science": 52, 
    "Web Development": 34, 
    "Machine Learning": 41, 
    "Cloud Computing": 29, 
    "Cyber Security": 33, 
    "DBMS": 48, 
    "Networking": 26, 
} 
"Operating Systems": 37 
Tasks 
1. Display courses having more than 40 enrollments.  
2. Find the most and least popular courses.  
3. Calculate total enrollments.  
4. Create lists:  
o High Demand (>40)  
o Medium Demand (30–40)  
o Low Demand (<30)  
5. Count courses requiring promotional activities (<35 enrollments).  """

enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}

# -----------------------------
# 1. Courses having > 40 enrollments
# -----------------------------
print("Courses with more than 40 enrollments:")
for course in enrollment:
    if enrollment[course] > 40:
        print(course, enrollment[course])

print("\n")

# -----------------------------
# 2. Most and least popular courses (NO max/min)
# -----------------------------
first_course = True

max_course = ""
min_course = ""
max_value = 0
min_value = 0

for course in enrollment:
    value = enrollment[course]

    if first_course:
        max_value = value
        min_value = value
        max_course = course
        min_course = course
        first_course = False
    else:
        if value > max_value:
            max_value = value
            max_course = course

        if value < min_value:
            min_value = value
            min_course = course

print("Most popular course:", max_course, max_value)
print("Least popular course:", min_course, min_value)

print("\n")

# -----------------------------
# 3. Total enrollments (NO sum())
# -----------------------------
total = 0

for course in enrollment:
    total = total + enrollment[course]

print("Total enrollments:", total)

print("\n")

# -----------------------------
# 4. Categorization lists
# -----------------------------
high_demand = []
medium_demand = []
low_demand = []

for course in enrollment:
    value = enrollment[course]

    if value > 40:
        high_demand.append(course)

    elif value >= 30 and value <= 40:
        medium_demand.append(course)

    else:
        low_demand.append(course)

print("High Demand (>40):", high_demand)
print("Medium Demand (30–40):", medium_demand)
print("Low Demand (<30):", low_demand)

print("\n")

# -----------------------------
# 5. Courses needing promotion (<35)
# -----------------------------
promotion_count = 0
promotion_courses = []

for course in enrollment:
    if enrollment[course] < 35:
        promotion_count += 1
        promotion_courses.append(course)

print("Courses needing promotion (<35):", promotion_count)
print("List:", promotion_courses)