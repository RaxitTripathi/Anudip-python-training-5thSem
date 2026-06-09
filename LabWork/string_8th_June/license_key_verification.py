""" 9. License Key Verification System 
Problem Statement 
A software license key is entered: 
ABCD-EFGH-IJKL-MNOP 
Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.  
7. Display whether the key format is valid.  """

key="ABCD-EFGH-IJKL-MNOP"
print("License Key:", key)
# 1.Verify there are exactly 4 groups.  

groups=key.split("-")  #  6. Create a list containing all groups.
valid_group=0
if len(groups) == 4:
    valid_group=1

# 2. Verify each group contains exactly 4 characters. 
valid_character=0   
for character in groups:
    if len(character) == 4:
        valid_character =1
    else:
        valid_character=0
        break    

# 3. Count total letters. 
# 4. Count vowels. 
count_letter=0
count_vowel=0

for character in key:
    if character.isalpha():
        count_letter +=1
    if character.lower() in "aeiou":
        count_vowel +=1

print("\nTotal letter:",count_letter)
print("Total vowel:",count_vowel)
# 5. Remove hyphens and display the merged key.          

merged_key=key.replace("-","")
print("\nMerged key:",merged_key)

#  6. Create a list containing all groups.
print("\nList conatining all groups:")
print(groups)


# 7. Display whether the key format is valid.

if valid_character ==1 and valid_group ==1:
    print("\nLicense Key Status:Valid")
else:
    print("\nLicense Key Status:InValid")    


""" output:

License Key: ABCD-EFGH-IJKL-MNOP

Total letter: 16
Total vowel: 4

Merged key: ABCDEFGHIJKLMNOP

List conatining all groups:
['ABCD', 'EFGH', 'IJKL', 'MNOP']

License Key Status:Valid """