""" 8. Online Quiz Performance 
Sample Data 
quiz_scores = { 
    "S001": 18, 
    "S002": 12, 
    "S003": 9, 
    "S004": 20, 
    "S005": 14, 
    "S006": 7, 
    "S007": 16, 
    "S008": 10, 
    "S009": 19, 
    "S010": 13 
} 
(Quiz is out of 20 marks.) 
Tasks 
• Display students scoring 15 or above.  
• Count students scoring below 10.  
• Find the top performer.  
• Create a list of students who passed (≥ 10 marks).  
• Calculate the class average.  """


quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Display students scoring 15 or above
print("Students scoring 15 or above:")
for student, score in quiz_scores.items():
    if score >= 15:
        print(student, ":", score)

# Count students scoring below 10
count = 0
for score in quiz_scores.values():
    if score < 10:
        count += 1

print("\nStudents scoring below 10:", count)

# Find the top performer
top_performer = None
highest_score = 0

for student in quiz_scores:
    if quiz_scores[student] > highest_score:
        highest_score = quiz_scores[student]
        top_performer = student

print("\nTop Performer:", top_performer)
print("Score:", highest_score)

# Create a list of students who passed (>= 10 marks)
passed_students = []
for student, score in quiz_scores.items():
    if score >= 10:
        passed_students.append(student)

print("\nPassed Students:")
print(passed_students)

# Calculate the class average (without sum())
total_marks = 0

for score in quiz_scores.values():
    total_marks += score

class_average = total_marks / len(quiz_scores)

print("\nClass Average:", class_average)