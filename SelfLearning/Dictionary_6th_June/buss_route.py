""" 7. Bus Route Passenger Analysis 
Sample Data 
passengers = { 
    "Stop1": 12, 
    "Stop2": 25, 
    "Stop3": 18, 
    "Stop4": 32, 
    "Stop5": 9, 
    "Stop6": 28, 
    "Stop7": 14, 
    "Stop8": 7, 
    "Stop9": 21, 
    "Stop10": 16 
} 
Tasks 
• Display stops having more than 20 passengers.  
• Count stops with fewer than 10 passengers.  
• Find the busiest stop.  
• Create a list of stops requiring an extra bus (passengers > 25).  
• Calculate the average number of passengers.  """


passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Display stops having more than 20 passengers
print("Stops having more than 20 passengers:")
for stop, count in passengers.items():
    if count > 20:
        print(stop, ":", count)

# Count stops with fewer than 10 passengers
low_count = 0
for count in passengers.values():
    if count < 10:
        low_count += 1

print("\nStops with fewer than 10 passengers:", low_count)

# Find the busiest stop

busiest_stop = None
max_passengers = 0

for stop in passengers:
    if passengers[stop] > max_passengers:
        max_passengers = passengers[stop]
        busiest_stop = stop

print("Busiest Stop:", busiest_stop)
print("Passengers:", max_passengers)


# Create a list of stops requiring an extra bus (passengers > 25)
extra_bus = []
for stop, count in passengers.items():
    if count > 25:
        extra_bus.append(stop)

print("\nStops requiring an extra bus:")
print(extra_bus)

# Calculate the average number of passengers (without sum())
total_passengers = 0

for count in passengers.values():
    total_passengers += count

average_passengers = total_passengers / len(passengers)

print("\nAverage number of passengers:", average_passengers)