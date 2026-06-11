""" Problem 3: Smart Parking Management System 
Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.  """

parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
]


    
    # 1. Display vacant parking slot numbers.
count=0
vacant_count=0
occupied_count=0

print("Vacant Parking Slots:")
for slot in parking_slots:
    if slot.lower() == "vacant":
        print(count,end="")
        vacant_count +=1

    else:
        occupied_count +=1    
    count +=1

    

    # 2. Count occupied and vacant slots   
            
print("Occupied Slots: ",occupied_count)
print("Vacant slots:",vacant_count)

# 3. Allocate the first vacant slot to a new vehicle. 

print("First vacant slot to a new vehicle:")
count_first=1
for slot in parking_slots:
    if slot == "Vacant":
        print(count_first)
        break
    count_first +=1  

#  4. Calculate parking occupancy percentage.     

print("Parking occupancy:",occupied_count*100/len(parking_slots))

# 5. Store updated parking information in parking.txt.


file=open("parking.txt","w")
file.write(parking_slots)
file.close()
