""" Problem 18: Student Attendance Percentage Calculator 
Problem Statement 
The attendance status of a student for 15 days is represented as follows: 
Sample Data 
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P') 
Tasks 
1. Count present days.  
2. Count absent days.  
3. Calculate attendance percentage.  
4. Determine whether attendance is below 75%.  
5. Display the attendance status.  """

attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P') 

present_count =0
absent_count =0

for day in attendance:
    if day == "P":
        present_count +=1
    elif day =="A":
        absent_count +=1

print("Present days",present_count)
print("Count absent days",absent_count)     

attendece_percentage =present_count *100 /len(attendance)

print(f"\nAttendence Percentage:{attendece_percentage:.2f}%")

print("\nAttendance Status: ")
if attendece_percentage < 75:
    print("Below 75%")
else:
    print("Above 75%")