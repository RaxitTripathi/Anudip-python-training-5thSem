'''Smart Parking System 
Problem Statement 
Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
• 1 = Occupied  
• 0 = Available  
Write a program to: 
• Count occupied and available slots.  
• Find the first available slot.  
• Display all available slot numbers.  
• Check whether parking occupancy exceeds 75%.'''

# Parking slots
slots = [1, 0, 1, 1, 0, 0, 1, 0]

occupied = 0
available = 0
available_slots = []
first_available = -1

# Count slots and find available slots
for i in range(len(slots)):
    if slots[i] == 1:
        occupied += 1
    else:
        available += 1
        available_slots.append(i + 1)  # Slot numbers start from 1

        if first_available == -1:
            first_available = i + 1

# Display results
print("Occupied Slots:", occupied)
print("Available Slots:", available)

if first_available != -1:
    print("First Available Slot:", first_available)
else:
    print("No Available Slot")

print("Available Slot Numbers:", available_slots)

# Check occupancy percentage
occupancy = (occupied / len(slots)) * 100

print("Occupancy Percentage:", occupancy, "%")

if occupancy > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")
