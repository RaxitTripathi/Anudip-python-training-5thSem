# Problem Statement 
# A flight reservation system stores passenger records as tuples: 
# bookings = ( 
#     ("P101", "Delhi", "Confirmed"), 
#     ("P102", "Mumbai", "Waiting"), 
#     ("P103", "Delhi", "Confirmed"), 
#     ("P104", "Chennai", "Cancelled"), 
#     ("P105", "Mumbai", "Confirmed"), 
#     ("P106", "Delhi", "Waiting") 
# ) 
# Where: 
# • Passenger ID  
# • Destination  
# • Booking Status  
# Tasks 
# Write a Python program to: 
# 1. Display all passengers whose booking status is Confirmed.  
# 2. Count the number of passengers travelling to Delhi.  
# 3. Count Confirmed, Waiting, and Cancelled bookings separately.  
# 4. Create a list containing passenger IDs with Waiting status.  
# 5. Determine which destination has the highest number of bookings.

# Flight bookings tuple
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display confirmed passengers
print("Confirmed Passengers:")
for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking[0],booking[1])

# 2. Count passengers travelling to Delhi
delhi_count = 0
for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1

print("\nPassengers travelling to Delhi:", delhi_count)

# 3. Count booking statuses
confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed += 1
    elif booking[2] == "Waiting":
        waiting += 1
    elif booking[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed :", confirmed)
print("Waiting :", waiting)
print("Cancelled :", cancelled)

# 4. Create list of waiting passenger IDs
waiting_ids = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_ids.append(booking[0])

print("\nWaiting List:")
print(waiting_ids)

# 5. Find destination with highest bookings
delhi_count = 0
mumbai_count = 0
chennai_count = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1
    elif booking[1] == "Mumbai":
        mumbai_count += 1
    elif booking[1] == "Chennai":
        chennai_count += 1

if delhi_count > mumbai_count and delhi_count > chennai_count:
    print("\nMost Booked Destination:\nDelhi")
    

elif mumbai_count > delhi_count and mumbai_count > chennai_count:
    print("\nMost Booked Destination:\nMumbai")

else:
    print("\nMost Booked Destination:\nChennai")
    