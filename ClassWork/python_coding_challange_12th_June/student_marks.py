	

# Question : Write a program to maintain a dictionary of student marks. Allow the user to add, update, and delete records using selection statements.

student_dict={}
while(True):
    user_input=int(input('''Select an option
1->ADD
2->Update
3->Delete
4->Exit'''))
    
    if user_input ==1:
        student_name=input("Enter Student Name:")
        student_marks=input("Enter student Marks:")

        student_dict[student_name]=student_marks

    elif user_input ==2:
        update_input=input("Enter Student Name:").lower()
        update_marks=int(input("Enter update marks:"))
        if update_input in student_dict.keys():
            student_dict[update_input]=  update_marks

        else:
            print("Student not found")

    elif user_input ==3:
        delete_input=input("Enter Student Name:").lower()
        if delete_input in student_dict.keys():
            del student_dict[delete_input]

        else:
            print("Student not found")

    elif user_input ==4:
        print("Exiting")
        break

    else:
        print("Invalid Input:")        



    

