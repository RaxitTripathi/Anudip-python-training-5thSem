'''Student Attendance Tracker 
Problem Statement 
Attendance for 15 days is recorded as: 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
Write a program to: 
• Count present and absent days.  
• Calculate attendance percentage.  
• Determine eligibility (minimum 75% attendance).  
• Display positions where the student was absent. '''

# Attendance record
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = 0
absent = 0

# Count present and absent days
for status in attendance:
    if status == 'P':
        present += 1
    else:
        absent += 1

print("Present Days:", present)
print("Absent Days:", absent)

# Calculate attendance percentage
attendance_percentage = (present / len(attendance)) * 100
print("Attendance Percentage:", attendance_percentage, "%")

# Check eligibility
if attendance_percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

# Display absent positions
print("Absent on Day Numbers:")
for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)