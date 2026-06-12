""" Problem 16: File Copy Utility 
Problem Statement 
A company wants to maintain backups of important documents. Create a program to copy the contents of one file into another. 

Sample Input/Data 
Source File (notes.txt) 
Python supports file handling. 
Functions improve code reusability. 
Dictionaries store data in key-value pairs. 
Tasks 
1. Read the contents of the source file.  
2. Copy the entire content to another file named backup.txt.  
3. Display a success message.  
4. Verify whether both files contain the same number of lines.   """


with open("notes.txt","r") as file:
#  1. Read the contents of the source file.     
    notes=file.read()
    print(notes)
    line=notes.split("\n")

with open("backup.txt","w") as file:
    # 2. Copy the entire content to another file named backup.txt.
    copy_content=notes
    file.write(copy_content)
    # 3. Display a success message.
    print("\nFile copy sucesss")


with open("backup.txt","r") as file:
    backup_notes =file.read()
    backup_line =backup_notes.split("\n")

print("\nSource File Lines:",len(line))
print("Backup File Lines:",len(backup_line))
if len(line) == len(backup_line):
    print("Verification Status: Successful")    


""" output:

Python supports file handling. 
Functions improve code reusability. 
Dictionaries store data in key-value pairs. 

File copy sucesss

Source File Lines: 3
Backup File Lines: 3
Verification Status: Successful """