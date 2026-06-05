''' Problem Statement 
A customer's transactions are stored as: 
transactions = [5000, -2000, 3000, -1000, -500, 7000] 
Positive values represent deposits and negative values represent withdrawals. 
Write a program to: 
 1. Calculate the current balance.  
 2. Count total deposits and withdrawals.  
 3. Find the largest deposit and largest withdrawal.   
 4. Create separate lists for deposits and withdrawals. '''


#Given list
transactions = [5000, -2000, 3000, -1000, -500, 7000] 


total_deposite=0
total_withdrawl=0
current_balance=0

#Let
largest_deposite=transactions[0]
largest_withdrawl=transactions[0]

#Stores both at differnt list
deposite_list=[]
withdrawl_list=[]

for i in transactions:
    #Find current balance
    current_balance +=i

#Cheak total count and append to list 
    if(i<0):
        total_withdrawl += 1
        withdrawl_list.append(i)
    else:
        total_deposite +=1
        deposite_list.append(i)

#Find largest deposite and withdrawl
    if(i>largest_deposite):
        largest_deposite=i
    elif(i<largest_withdrawl):
        largest_withdrawl=i

#Print desired output
print("Current Balance:",current_balance)
print("Total Deposite:",total_deposite)
print("Total Withdrawl:",total_withdrawl)
print("Deposits:",deposite_list)
print("Withdrawals:",withdrawl_list)
print("Largest Deposit:",largest_deposite)
print("Largest Withdrawal:",largest_withdrawl)

