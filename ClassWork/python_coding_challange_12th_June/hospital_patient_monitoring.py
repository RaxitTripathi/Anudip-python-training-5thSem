""" Problem 9: Hospital Patient Monitoring System 
Problem Statement 
Patient heart rates are recorded below. 
Sample Data 
heart_rate = { 
    "P101": 72, 
    "P102": 105, 
    "P103": 88, 
    "P104": 120, 
    "P105": 65, 
    "P106": 98, 
    "P107": 110, 
    "P108": 70, 
    "P109": 85, 
    "P110": 130 
} 
Tasks 
1. Display critical patients (heart rate >100).  
2. Find highest and lowest heart rate.  
3. Calculate average heart rate.  
4. Count stable patients (60–100 bpm).  """

heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# 1. Critical patients (heart rate > 100)
print("Critical Patients:")
for patient, rate in heart_rate.items():
    if rate > 100:
        print(patient, ":", rate)

# 2. Highest and Lowest heart rate
highest = -1
lowest = 999

for rate in heart_rate.values():
    if rate > highest:
        highest = rate

    if rate < lowest:
        lowest = rate

print("\nHighest Heart Rate:", highest)
print("Lowest Heart Rate:", lowest)

# 3. Average heart rate
total = 0
count = 0

for rate in heart_rate.values():
    total += rate
    count += 1

average = total / count

print("Average Heart Rate:", average)

# 4. Stable patients (60–100 bpm)
stable_count = 0

for rate in heart_rate.values():
    if 60 <= rate <= 100:
        stable_count += 1

print("Stable Patients:", stable_count)


""" # output:

Critical Patients:
P102 : 105
P104 : 120
P107 : 110
P110 : 130

Highest Heart Rate: 130
Lowest Heart Rate: 65
Average Heart Rate: 94.3
Stable Patients: 6 """