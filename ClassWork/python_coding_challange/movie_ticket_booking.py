""" Problem 7: Movie Ticket Booking System 
Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage. """

tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 

# 1. Display available seats.  
booked_count=0
available_count=0

print("Available Seats:")
for seat,status in tickets.items():
    if status == "Available":
        print(seat)
        available_count +=1
    else:
        booked_count +=1    


# 2. Count booked and available seats.  

print("\nBooked Seats:",booked_count) 
print("Available Seats:",available_count)


# 3. Reserve the first available seat. 

for seat,status in tickets.items():
    if status == "Available":
        print("\nSeat",seat<"Reserved Successfully.")
        break     

# 5. Calculate hall occupancy percentage.    
hall_occupancy =booked_count*100/(booked_count+available_count)
print("Hall Occupancy Percentage: ",hall_occupancy)

# 4. Save updated booking details to tickets.txt. 

file = open("tickets.txt", "w")

for seat, status in tickets.items():
    file.write(seat + "," + status + "\n")

file.close()

print("\nUpdated booking details saved to tickets.txt")