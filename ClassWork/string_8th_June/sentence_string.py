#Wap a program to input a sentence from user and count the number of special char present in the sentence

user_input=input("Enter an sentence:")

special_count=0

for letter in user_input:
    if letter.isalnum():
        continue
    else:
        special_count +=1

print("Total special character:",special_count)
