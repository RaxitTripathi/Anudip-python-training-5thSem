""" Problem 2: Hospital Patient Record Management System 
Problem Statement 
A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 
1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt.   """

while(True):
    user=int(input('''1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt. 
6. Exit
'''))

# 1. Display all patient records.
    if user ==1:
        file=open("patients.txt",'r')
        print("Patient records:",file.read())
        file.close() 

# 2. Display critical patients.
    elif(user ==2):
        file=open("patients.txt",'r')
        data_read=file.read()
        data=data_read.split("\n")
        print("Crictical Patients:")
        for patient in data:
            new_data=patient.split(",")
            if new_data[2].lower() =="critical":
                print(new_data[0],new_data[1])
        file.close()         
        
# 3. Count patients under each status. 
    elif user ==3:
        normal=0
        stable=0
        critical=0
        file=open("patients.txt",'r')
        data_read=file.read()
        data=data_read.split("\n")
        for patient in data:
            new_data=patient.split(",")
            if new_data[2].lower() =="critical":
                critical +=1
            elif new_data[2].lower() =="stable":
                stable +=1
            else:
                normal +=1
        print("Normal patient:",normal)
        print("Stable patient:",stable)
        print("Critical patient:",critical)   
        file.close()          

# 4. Search patient details using Patient ID. 
    elif user ==4:
        patient_detail=input("Enter Patient Id:")
        file=open("patients.txt",'r')
        data_read=file.read()
        data=data_read.split("\n")
        print("Pateint Found:")
        for patient in data:
            new_data=patient.split(",")
            if new_data[0] == patient_detail:
                print(new_data[0],new_data[1],new_data[2])
        file.close() 
# Save critical patient records to critical_patients.txt.       

    elif user ==5:
        file=open("patients.txt",'r')
        data_read=file.read()
        data=data_read.split("\n")
        critical_patient =""
        for patient in data:
            new_data=patient.split(",")
            if new_data[2].lower() =="critical":
                critical_patient +=new_data[0],new_data[1],new_data[2],"\n"
        file_w=open("critical_patients.txt","w")
        file_w.write(critical_patient)
        print(" Critical Patient Report Generated Successfully.")

        file.close()  
        file_w.close()      

    elif user ==6:
        break

    else:
        print("Invalid Input")