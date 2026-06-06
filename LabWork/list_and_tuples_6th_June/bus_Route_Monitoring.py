'''Bus Route Monitoring 
Problem Statement 
Passenger count at each stop: 
passengers = [12, 18, 25, 30, 28, 15, 8] 
Write a program to: 
• Find the busiest stop.  
• Display stops with fewer than 10 passengers.  
• Calculate average passengers.  
• Determine whether any stop exceeded 25 passengers. '''

# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
max_passengers = passengers[0]
busiest_stop = 1

for i in range(len(passengers)):
    if passengers[i] > max_passengers:
        max_passengers = passengers[i]
        busiest_stop = i + 1

print("Busiest Stop:", busiest_stop)
print("Passengers at Busiest Stop:", max_passengers)

# Display stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Calculate average passengers
total = 0
for p in passengers:
    total += p

average = total / len(passengers)
print("\nAverage Passengers:", average)

# Check if any stop exceeded 25 passengers
exceeded = False

for p in passengers:
    if p > 25:
        exceeded = True
        break

if exceeded:
    print("At least one stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")