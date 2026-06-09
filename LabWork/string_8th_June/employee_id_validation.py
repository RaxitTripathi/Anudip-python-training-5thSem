""" 1. Employee ID Validation and Analysis System 
Problem Statement 
A company generates employee IDs in the following format: 
EMP2026ANUJ458 
Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  
6. Create a list containing  all digits present in the ID. 
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid.   """

emp_id = "EMP2026ANUJ458"

# 1. Count the number of uppercase letters.  
count_upper=0

# 2. Count the number of digits.
count_digits=0

for letter in emp_id:
    if letter.isupper():
        count_upper +=1
    elif letter.isdigit():    
        count_digits +=1

print("Number of uppercase letters:",count_upper)
print("\nNumber of digits:",count_digits)

print("\nJoining year:",emp_id[3:7])

print("\nEmployee name:",emp_id[7:-3])


# 6. Create a list containing  all digits present in the ID. 
digit_list=[]
for letter in emp_id:
    if letter.isdigit():
        digit_list.append(letter)

print("\nDigit List:",digit_list)

# 7. Find the sum of all digits present in the ID. 

sum_digit=0
for digit in digit_list:
    sum_digit += int(digit)

print("\nSum of Digits:",sum_digit)    

""" 5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  """


# 8. Display whether the ID is valid or invalid.
if (emp_id.startswith("EMP") and
    emp_id[3:7].isdigit() and
    len(emp_id[3:7]) == 4 and
    emp_id[-3:].isdigit()):

    print("ID Status: Valid")
else:
    print("ID Status: Invalid")

""" output:

Number of uppercase letters: 7

Number of digits: 7

Joining year: 2026

Employee name: ANUJ

Digit List: ['2', '0', '2', '6', '4', '5', '8']

Sum of Digits: 27
ID Status: Valid """