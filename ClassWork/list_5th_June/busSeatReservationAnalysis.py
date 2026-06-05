'''A bus has seats represented as: 
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
Where: 
• 1 → Seat Booked  
• 0 → Seat Available  
Write a program to: 
1. Count booked and available seats.  
2. Find the first available seat and stop searching immediately.  
3. Create a list of all available seat numbers.  
4. Determine whether the bus is more than 70% occupied. '''


seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

available_seats = 0
booked_seats = 0
available_seats_no = []
first_available = -1

for i in range(len(seats)):
    if seats[i] == 0:
        available_seats += 1
        available_seats_no.append(i + 1)  # seat number
    else:
        booked_seats += 1

# first available seat (stop immediately)
for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1
        break

print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)

print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats_no)

occupancy = (booked_seats / len(seats)) * 100
print("Bus Occupancy:", occupancy)

if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
