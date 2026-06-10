""" Assignment 1: Password Security Analyzer 
Problem Statement 
A cybersecurity company wants to analyze user passwords before allowing account creation. 
The system should accept at least 15 passwords and generate a security report. 
Requirements 
For each password: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Check minimum length (8 characters).  
6. Check if spaces exist.  
7. Determine password strength:  
o Strong  
o Medium  
o Weak  
8. Display repeated characters.  
9. Count vowels and consonants.  
10. Identify the most frequently occurring character.  
Challenge 
Generate a report showing: 
Total Passwords Analyzed 
Strong Passwords 
Medium Passwords 
Weak Passwords
 """

# Report counters
strong = 0
medium = 0
weak = 0

# Analyze 15 passwords
for i in range(15):

    print("\nPassword", i + 1)
    password = input("Enter Password: ")

    upper = 0
    lower = 0
    digits = 0
    special = 0
    vowels = 0
    consonants = 0
    spaces = 0

    # Count character types
    for ch in password:

        if ch.isupper():
            upper += 1

        elif ch.islower():

            lower += 1

        elif ch.isdigit():
            digits += 1

        elif ch == " ":
            spaces += 1

        else:
            special += 1

        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    # Calculate length
    length = 0

    for ch in password:
        length += 1

    # Find repeated characters
    repeated = ""

    for ch in password:

        count = 0

        for x in password:
            if ch == x:
                count += 1

        if count > 1 and ch not in repeated:
            repeated += ch + " "

    # Find most frequent character
    max_count = 0
    most_frequent = ""

    for ch in password:

        count = 0

        for x in password:
            if ch == x:
                count += 1

        if count > max_count:
            max_count = count
            most_frequent = ch

    # Determine password strength
    if length >= 8 and upper > 0 and lower > 0 and digits > 0 and special > 0 and spaces == 0:

        strength = "Strong"
        strong += 1

    elif length >= 8 and spaces == 0:

        strength = "Medium"
        medium += 1

    else:

        strength = "Weak"
        weak += 1

    # Display password analysis
    print("\n----- Analysis -----")
    print("Uppercase Letters :", upper)
    print("Lowercase Letters :", lower)
    print("Digits :", digits)
    print("Special Characters :", special)
    print("Length :", length)

    if spaces > 0:
        print("Spaces Exist : Yes")
    else:
        print("Spaces Exist : No")

    print("Password Strength :", strength)
    print("Repeated Characters :", repeated)
    print("Vowels :", vowels)
    print("Consonants :", consonants)
    print("Most Frequent Character :", most_frequent)

# Generate final report
print("\n========== SECURITY REPORT ==========")
print("Total Passwords Analyzed :", 15)
print("Strong Passwords :", strong)
print("Medium Passwords :", medium)
print("Weak Passwords :", weak)