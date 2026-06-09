""" 4. Vehicle Number Plate Verification 
Problem Statement 
A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid.  """

plate = "MH12AB4589"

# 1. Extract state code
state_code = plate[0:2]
print("State Code:", state_code)

# 2. Extract district code
district_code = plate[2:4]
print("District Code:", district_code)

# 3. Extract vehicle series
vehicle_series = plate[4:6]
print("Vehicle Series:", vehicle_series)

# 4. Extract vehicle number
vehicle_number = plate[6:]
print("Vehicle Number:", vehicle_number)

# 5. Count letters and digits separately
letter_count = 0
digit_count = 0

for ch in plate:
    if ch.isalpha():
        letter_count += 1
    elif ch.isdigit():
        digit_count += 1

print("Letters:", letter_count)
print("Digits:", digit_count)

# 6. Verify number plate format

# First 2 characters must be alphabets
first_part = plate[0:2].isalpha()

# Next 2 must be digits
second_part = plate[2:4].isdigit()

# Next 2 must be alphabets
third_part = plate[4:6].isalpha()

# Last 4 must be digits
fourth_part = plate[6:].isdigit()

# 7. Display whether number plate is valid
if (len(plate) == 10 and
    first_part and
    second_part and
    third_part and
    fourth_part):

    print("Number Plate Status: Valid")

else:
    print("Number Plate Status: Invalid")

""" output:

State Code: MH
District Code: 12
Vehicle Series: AB
Vehicle Number: 4589
Letters: 4
Digits: 6
Number Plate Status: Valid """