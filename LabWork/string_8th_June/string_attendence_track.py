""" 8. String-Based Attendance Tracker 
Problem Statement 
Attendance of a student for 15 days is represented as: 
PPAPPPAAPPPPAPP 
Where: 
• P = Present  
• A = Absent  
Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%.  """

attendence="PPPP"

print("Attendence:",attendence)
# 1. Count Present and Absent days. 

count_present=0
count_absent=0
for report in attendence:
    if(report == "P"):
        count_present +=1
    else:
        count_absent +=1

print("\nPresent Days:",count_present)
print("Absent Days:",count_absent)


# 2. Calculate attendance percentagea. 

attendence_percentage=(count_present /len(attendence))*100
print("\nAttendance Percentage:",attendence_percentage)

# 3. Find the longest consecutive streak of Presence.  
# 4. Find the longest consecutive streak of Absence.  

highest_present_streak=0
current_present_streak=0
highest_absent_streak=0
current_absent_streak=0
for report in attendence:
    if report == "P":
        current_present_streak += 1
        current_absent_streak = 0

        if current_present_streak > highest_present_streak:
            highest_present_streak = current_present_streak

    else:
        current_absent_streak += 1
        current_present_streak = 0

        if current_absent_streak > highest_absent_streak:
            highest_absent_streak = current_absent_streak   

print("\nLongest Present Streak: ",highest_present_streak)   
print("Longest Absent Streak:",highest_absent_streak)       

# 5. Determine whether attendance is below 75%.
if attendence_percentage <75:
    print("\nAttendence Status:Below 75%")
else:    
    print("\nAttendence Status:Above 75%")



""" output:

Attendence: PPAPPPAAPPPPAPP

Present Days: 11
Absent Days: 4

Attendance Percentage: 73.33333333333333

Longest Present Streak:  4
Longest Absent Streak: 2

Attendence Status:Below 75% """