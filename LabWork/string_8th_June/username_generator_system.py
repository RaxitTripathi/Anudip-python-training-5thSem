""" 
7. Username Generator System 
Problem Statement 
A student enters: 
Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics.  """

name="Rahul Sharma"

# 1. Remove spaces. 
username=name.replace(" ","")

# 2. Convert to lowercase.
username=username.lower()

# 3. Append current year (2026).
username += "2026"


# 4. If username length exceeds 12, keep only first 12 characters.  
if len(username) > 12:
    username=username[0:12]


# 5. Count vowels in the generated username. 

count_vowels=0
count_consonants=0

for letter in username:
    if letter.isalpha():
        if letter in "aeiou":
            count_vowels +=1
        else:
            count_consonants +=1    



# 7. Display username statistics.

print("Original Name:", name)
print()
print("Generated Username:")
print(username)
print()
print("Username Length:", len(username))
print()
print("Vowels:", count_vowels)
print("Consonants:", count_consonants)
print()
print("Status: Username Generated Successfully")

""" output:

Original Name: Rahul Sharma

Generated Username:
rahulsharma2

Username Length: 12

Vowels: 4
Consonants: 7

Status: Username Generated Successfully """