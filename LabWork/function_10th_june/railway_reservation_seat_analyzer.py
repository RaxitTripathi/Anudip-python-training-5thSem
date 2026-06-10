""" 1. Railway Reservation Seat Analyzer Problem Statement A railway coach has seats represented as follows: 
seats = [     "Booked", "Available", "Booked", "Booked",     "Available", "Available", "Booked", "Available",     "Booked", "Booked", "Available", "Booked" ] 
Requirements Create the following functions: 
1. count_seats(seats) Returns the number of booked and available seats.
2. first_available(seats) Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) Returns the percentage of occupied seats. 
4. display_available_seats(seats) Displays all available seat numbers.  """


# 1. count_seats(seats) Returns the number of booked and available seats.
def count_seats(seats):
    available_count=0
    booked_count=0
    for seat in seats:
        if seat.lower() == "available":
            available_count +=1
        else:
            booked_count +=1
    return (available_count,booked_count)            

# 2. first_available(seats) Returns the seat number of the first available seat.
def first_available(seats):
    first_seat=1
    for seat in seats:
        if seat.lower() == "available":
            break
        first_seat +=1
    return first_seat    

# 3. occupancy_percentage(seats) Returns the percentage of occupied seats. 
def ocuupancy_percentage(seats):
    total_seats=len(seats)
    count_booked=0
    for seat in seats:
        if seat.lower() == "booked":
            count_booked +=1
    return count_booked*100/total_seats        

# 4. display_available_seats(seats) Displays all available seat numbers.
def display_available_seats(seats):
    count_available=1
    print("\nAvailable seats:")
    for seat in seats:
        if seat.lower() == "available":
            print(count_available,end=" ")
            
        count_available +=1    
        

#Given Data
seats = [     "Booked", "Available", "Booked", "Booked",     "Available", "Available", "Booked", "Available",     "Booked", "Booked", "Available", "Booked" ] 

available,booked=count_seats(seats)
print("Booked seats:",booked)
print("Available seats:",available)


print("\nFirst Available seat:",first_available(seats))

print("\nOccupancy percentage:",ocuupancy_percentage(seats),"%")

display_available_seats(seats)

""" 
output:

Booked seats: 7
Available seats: 5

First Available seat: 2

Occupancy percentage: 58.333333333333336 %

Available seats:
2 5 6 8 11  """


