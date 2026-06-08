#Wap to input a string or sentence from user and count no of char present in it without using len func


user_input=input("Enter sentence: ")
count_user =0
for word in user_input:
    count_user +=1
print("Total character:",count_user)        