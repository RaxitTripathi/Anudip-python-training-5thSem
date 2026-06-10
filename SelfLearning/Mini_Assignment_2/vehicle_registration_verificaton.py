""" Assignment 4: Vehicle Registration Verification System 
Problem Statement 
A transport department wants to verify vehicle registration numbers. 
Store at least 20 vehicle numbers. 
Example 
MH12AB4589 
DL05XY9988 
KA03PQ1234 
Requirements 
For each registration number: 
1. Extract state code.  
2. Extract district code.  
3. Extract series.  
4. Extract vehicle number.  
5. Count letters and digits.  
6. Validate format:  
o First 2 characters = Alphabets  
o Next 2 characters = Digits  
o Next 2 characters = Alphabets  
o Last 4 characters = Digits  
7. Display invalid registrations.  
8. Count vehicles state-wise.  
Challenge 
Generate a state-wise report: 
MH -> 6 Vehicles 
DL -> 4 Vehicles 
KA -> 5 Vehicles 
UP -> 5 Vehicles  """

# Vehicle Registration Verification System

vehicles = []


# STEP 1: INPUT 20 VEHICLES

for i in range(20):
    while True:
        v = input(f"Enter vehicle number {i+1}: ").strip().upper()
        if v != "":
            break
        print("Invalid input! Try again.")

    vehicles.append(v)

# To store state-wise vehicle count
state_count = {}

# To store invalid vehicle numbers
invalid_vehicles = []

print("\nVEHICLE ANALYSIS")
print("-" * 60)


# STEP 2: PROCESS EACH VEHICLE

for v in vehicles:

    print("\nVehicle:", v)

    
    # STEP 3: EXTRACT PARTS
    
    if len(v) != 10:
        print("Invalid Format (Length issue)")
        invalid_vehicles.append(v)
        continue

    state = v[0:2]        # First 2 characters → State code
    district = v[2:4]     # Next 2 digits → District code
    series = v[4:6]       # Next 2 letters → Series
    number = v[6:10]      # Last 4 digits → Vehicle number

    
    # STEP 4: COUNT LETTERS & DIGITS
    
    letters = 0
    digits = 0

    for ch in v:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1

    print("State Code:", state)
    print("District Code:", district)
    print("Series:", series)
    print("Vehicle Number:", number)
    print("Letters Count:", letters)
    print("Digits Count:", digits)
     
    # STEP 5: VALIDATE FORMAT
    
    valid = (
        state.isalpha() and
        district.isdigit() and
        series.isalpha() and
        number.isdigit()
    )

    if valid:
        print("Status: VALID")

        
        # STEP 6: STATE-WISE COUNTING
        
        if state in state_count:
            state_count[state] += 1
        else:
            state_count[state] = 1

    else:
        print("Status: INVALID")
        invalid_vehicles.append(v)


# STEP 7: DISPLAY INVALID VEHICLES

print("\nINVALID VEHICLE NUMBERS")
print("-" * 60)

for v in invalid_vehicles:
    print(v)


# STEP 8: STATE-WISE REPORT
print("\nSTATE-WISE REPORT")
print("-" * 60)

for state, count in state_count.items():
    print(state, "->", count, "Vehicles")