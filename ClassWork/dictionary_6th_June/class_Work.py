# Class Work: Dictionary  Create Attendance tracker of 30 students. Ask the user to input roll number of student and also input whether student is Present or Absent. Store the data in dictionary where roll number will be used as a key and Attendance as Value. Display the roll number of students who are Present 

class_report={}
student_no=30
while(student_no):
    user_input_rollno=int(input("Enter roll no:"))
    user_input_attendence=input("Enter attendence:").lower()
    if user_input_attendence != "present" and user_input_attendence != "absent":
        print("Present or Absent so reinput")
        student_no +=1 
    class_report.update({user_input_rollno:user_input_attendence,}) 
    student_no -= 1


print("Roll no of present student:")
for student in class_report:
    if(class_report[student] == "present"):
        print(student)      
