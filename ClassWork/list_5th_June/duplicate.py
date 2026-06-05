#Wap to create a list of 20 number given by user.Ask the user to input any other number.Remove all the duplicate entries of this no. from the list 
user_list = []
print("Enter numbers:")

for i in range(20):
    user_list.append(int(input()))

user_remove_number = int(input("Enter number to remove duplicates of: "))

if user_remove_number not in user_list:
    exit("Number not present in list")


found = False
new_list = []

for num in user_list:
    if num == user_remove_number:
        if not found:
            new_list.append(num)  # keep first occurrence
            found = True
        
    #skip duplicates
    else:
        new_list.append(num)

print(new_list)       