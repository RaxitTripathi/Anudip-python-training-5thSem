'''Problem Statement 
Passenger records: 
passengers = [ 
    ("Anuj", "Confirmed"), 
    ("Rahul", "Waiting"), 
    ("Priya", "Confirmed"), 
    ("Amit", "Waiting"), 
    ("Neha", "Confirmed") 
] 
Write a program to: 
• Display all waiting-list passengers.  
• Count confirmed and waiting passengers.  
• Find whether a specific passenger has a confirmed ticket.  
• Create separate lists for confirmed and waiting passengers.'''

passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Display all waiting-list passengers
print("Waiting-list passengers:")
for passenger in passengers:
    if passenger[1] == "Waiting":
        print(passenger[0])

# Count confirmed and waiting passengers
confirmed_count = 0
waiting_count = 0

for passenger in passengers:
    if passenger[1] == "Confirmed":
        confirmed_count += 1
    else:
        waiting_count += 1

print("\nConfirmed passengers:", confirmed_count)
print("Waiting passengers:", waiting_count)

# Find whether a specific passenger has a confirmed ticket
name = input("\nEnter passenger name: ").lower()

found = False

for passenger in passengers:
    if passenger[0].lower() == name and passenger[1] == "Confirmed":
        found = True
        break

if found:
    print(name, "has a confirmed ticket.")
else:
    print(name, "does not have a confirmed ticket.")

# Create separate lists for confirmed and waiting passengers
confirmed_list = []
waiting_list = []

for passenger in passengers:
    if passenger[1] == "Confirmed":
        confirmed_list.append(passenger[0])
    else:
        waiting_list.append(passenger[0])

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)



