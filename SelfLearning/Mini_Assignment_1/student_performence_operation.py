

#1. Display all student records

def display_all_students(students):
    for student in students:
        print(students[student])


#2.  Search a student using Student ID. 

def search_student(search_id,students):
    if search_id in students:
        print("Name :", students[search_id]["name"])
        print("Marks:", students[search_id]["marks"])
    else:
        print("Student Not found")    

# 3. Add a new student.  

def new_student(sid,students):
    if sid in students:

        print("Student ID Already Exists")

    else:

        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        students[sid] = {
            "name": name,
            "marks": marks
        }

        print("Student Added Successfully")

# 4. Update marks of an existing student.

def update_marks(sid,students):
    if sid in students:

        marks = float(input("Enter New Marks: "))
        students[sid]["marks"] = marks

        print("Marks Updated Successfully")

    else:
        print("Student Not Found")          

# 5. Delete a student.        

def delete_students(sid,students):
    if sid in students:
        del students[sid]
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")

# 6. Find topper and lowest scorer.        

def position_students(students):

    topper_id = None
    lowest_id = None

    for sid, data in students.items():

        if topper_id is None or data["marks"] > students[topper_id]["marks"]:
            topper_id = sid

        if lowest_id is None or data["marks"] < students[lowest_id]["marks"]:
            lowest_id = sid

    print("\nTopper")
    print(topper_id, students[topper_id]["name"], students[topper_id]["marks"])

    print("\nLowest Scorer")
    print(lowest_id, students[lowest_id]["name"], students[lowest_id]["marks"])

# 7. Calculate class average.    
def average_class(students):
    total = 0

    for data in students.values():
        total += data["marks"]

    average = total / len(students)

    print("Class Average =", round(average, 2))


#8. Count pass and fail.
def count_students(students):
        
        pass_count = 0
        fail_count = 0

        for data in students.values():

            if data["marks"] >= 50:
                pass_count += 1
            else:
                fail_count += 1

        print("Pass Students =", pass_count)
        print("Fail Students =", fail_count)

# 9. Generate grades:  
# o A (90+)  
# o B (75–89)  
# o C (50–74)  
# o F (<50)          

def grade_students(students):
        print("\nGrades Report")

        for sid, data in students.items():

            marks = data["marks"]

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            else:
                grade = "F"

            print(f"{sid} | {data['name']} | {marks} | Grade {grade}")

# 10. Above Average Students

def above_average(students):
    total = 0

    for sid in students:
        total += students[sid]["marks"]

    avg = total / len(students)

    for sid in students:

        if students[sid]["marks"] > avg:

            print(
                sid,
                students[sid]["name"],
                students[sid]["marks"]
        )
            
# 11. Display top 5 performers.              
def top_5_students(students):

    temp = students.copy()

    print("\nTop 5 Performers")

    count = 0

    while count < 5 and len(temp) > 0:

        best_id = None

        for sid, data in temp.items():

            if best_id is None or data["marks"] > temp[best_id]["marks"]:
                best_id = sid

        print(best_id, temp[best_id]["name"], temp[best_id]["marks"])

        temp.pop(best_id)

        count += 1

# 12. Create a separate dictionary for scholarship students (marks > 85). 

def scholarship_student(students):
    # Scholarship students (marks > 85)

        # Scholarship students (marks > 85)

    scholarship = {}

    for sid, data in students.items():

        if data["marks"] > 85:
            scholarship[sid] = data

    print("\nScholarship Students")

    for sid, data in scholarship.items():
        print(sid, data["name"], data["marks"]) 