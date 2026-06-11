""" Problem 6: Employee Attendance Monitoring System 
Problem Statement 
Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance).  """

# Problem 6: Employee Attendance Monitoring System

# Read attendance records
file = open("attendance.txt", "r")
records = file.readlines()
file.close()

present_count = 0
absent_count = 0
absent_employees = []
award_employees = []

# Create absentee report file
report = open("absent_report.txt", "w")

for record in records:
    record = record.strip()

    emp_id, status = record.split(",")

    if status == "P":
        present_count += 1

        # Since only one day's data is given,
        # present employees are treated as 100% attendance.
        award_employees.append(emp_id)

    else:
        absent_count += 1
        absent_employees.append(emp_id)

        report.write(emp_id + "\n")

report.close()

# Calculate attendance percentage
total_employees = present_count + absent_count
attendance_percentage = (present_count / total_employees) * 100

# 1. Count present and absent employees.  
print("Present Employees:", present_count)
print("Absent Employees:", absent_count)

print("\nAbsent Employee IDs:")
for emp_id in absent_employees:
    print(emp_id)

print("\nAttendance Percentage:", attendance_percentage, "%")

print("\nEmployees Eligible for Attendance Awards:")
for emp_id in award_employees:
    print(emp_id)