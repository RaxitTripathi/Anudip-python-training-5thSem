""" Classwork : To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file. """

#Open file in read operation
file=open('sentences.txt','r')

if not file:
    exit("File not found:")

contents=file.read()

# 1. No. of Vowels in file.

count_vowel=0
count_extraspace=0
for content in contents:
    if content in "aeiou":   
        count_vowel +=1
    if "\n" in content:
        count_extraspace +=1

print("No of vowel:",count_vowel)
# 2. No. of characters into the file.

total_char=len(contents) - count_extraspace
print("No of characters:",total_char)

# 3. No. of lines into the file. 
print("Total no of line in a file:",count_extraspace+1)

file.close()

