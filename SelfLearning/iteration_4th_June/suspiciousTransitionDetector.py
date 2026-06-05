# Problem Statement: 
# Input transaction amounts continuously. 
# Stop when -1 is entered. 
# Count: 
# • Transactions above ₹50,000  
# • Transactions below ₹1,000  
# • Total transaction amount

count1=0
count2=0
total_amt=0
while(True):
    print("-1 for trasactions end")
    amount=int(input("Enter amount:"))

    if(amount<-1):
        print("Transaction amount can not be in negative")
        continue
        
    elif(amount==-1):
        break

    elif(amount>50000):
        count1+=1
        

    elif(amount<1000):
        count2+=1 

    
    total_amt+=amount    

print("Transactions above ₹50,000: ",count1)
print("Transactions below ₹1,000:",count2)
print("Total transaction amount:",total_amt)    