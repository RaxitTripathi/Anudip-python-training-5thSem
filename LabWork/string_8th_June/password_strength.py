""" 2. Password Strength Analyzer 
Problem Statement 
A user enters a password. 
Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately. """


password = "Python@2026!"

#Password Validation
if(len(password) < 8 ):
    exit("Password length smaller than 8 Not allowed")

# 1. Count uppercase letters
upper_count = 0

# 2. Count lowercase letters
lower_count = 0

# 3. Count digits
digit_count = 0

# 4. Count special characters
special_count = 0

# List for digits
digits = []

# List for special characters
special_chars = []

# Flags for password strength
has_upper = False
has_lower = False
has_digit = False
has_special = False


for ch in password:

    # Check uppercase
    if ch.isupper():
        upper_count += 1
        has_upper = True

    # Check lowercase
    elif ch.islower():
        lower_count += 1
        has_lower = True

    # Check digit
    elif ch.isdigit():
        digit_count += 1
        has_digit = True
        digits.append(ch)

    # Check special character
    else:
        special_count += 1
        has_special = True
        special_chars.append(ch)

# Display uppercase count
print("Uppercase Letters:", upper_count)

# Display lowercase count
print("Lowercase Letters:", lower_count)

# Display digit count
print("Digits:", digit_count)

# Display special character count
print("Special Characters:", special_count)

# 5. Display all digits separately
print("Digits Present:", digits)

# 6. Display all special characters separately
print("Special Characters Present:", special_chars)

# Check password strength
if (len(password) >= 8 and
    has_upper and
    has_lower and
    has_digit and
    has_special):

    print("Password Strength: Strong")

elif len(password) >= 8:
    print("Password Strength: Medium")

else:
    print("Password Strength: Weak")

""" output:

Uppercase Letters: 1
Lowercase Letters: 5
Digits: 4
Special Characters: 2
Digits Present: ['2', '0', '2', '6']
Special Characters Present: ['@', '!']
Password Strength: Strong """