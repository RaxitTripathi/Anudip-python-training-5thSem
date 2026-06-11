""" Problem 1: Smart Railway Reservation System 
Problem Statement 
A railway reservation system stores the booking status of seats in a train coach. 
Sample Data 
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
Tasks 
1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt.  
6. Display occupancy percentage.  


Sample Output 
Available Seats: 
2 4 7 9 
 
Booked Seats: 6 
Available Seats: 4 
 
Seat 2 Reserved Successfully. 
 
Occupancy Percentage: 70.0% 
 
Reservation Details Saved Successfully. """

#Given Data
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 


# 1. Display all available seat numbers.  
available_seat=0
booked_seat=0
print("Available seats:")
for seat in seats:
    if "available" in seats[seat].lower():
        print(seat,end=" ")
        available_seat +=1
    else:
        booked_seat +=1

# 2. Count booked and available seats. 

print("\nAvailable seats:",available_seat)
print("Booked seats:",booked_seat)

# 3. Reserve the first available seat. 

for seat in seats:
    if "available" in seats[seat].lower():
        print("Seat ",seat,"Reserved successfully")
        break
       

# 4. Cancel booking for a given seat number.  
user_input=int(input("Enter seat number:"))

for seat in seats:
    if seat == user_input:
        seats[seat] ="Available"
        break
    elif seats[user_input] == "Available":
        print("Seat already Available may be Wrong seat number ")    

# 5. Store the updated reservation status in reservations.txt.
file=open('reservations.txt','w')  
for seat in seats:
    file.writelines(str(seat))
    file.writelines(str(seats[seat]))
    file.writelines("\n")
file.close()     

# 6. Display occupancy percentage. 

print("Occupancy Percentage:",booked_seat*100/len(seats))


print("Reservation Details Saved Successfully.")