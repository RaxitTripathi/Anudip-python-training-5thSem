""" 2. Employee Performance Dashboard 
Problem Statement 
Employee performance scores are stored as: 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60) """

performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp, ":", score)

# 2. Count employees needing improvement (< 60)
count = 0
for score in performance.values():
    if score < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# 3. Find top performer (without max())
top_emp = None
top_score = 0

for emp, score in performance.items():
    if score > top_score:
        top_score = score
        top_emp = emp

print("\nTop Performer:")
print(top_emp, ":", top_score)

# 4. Calculate average performance score
total = 0

for score in performance.values():
    total += score

average = total / len(performance)

print("\nAverage Performance Score:", average)

# 5. Categorize employees
excellent = []
good = []
average_list = []
poor = []

for emp, score in performance.items():

    if score >= 90:
        excellent.append(emp)

    elif 75 <= score <= 89:
        good.append(emp)

    elif 60 <= score <= 74:
        average_list.append(emp)

    else:
        poor.append(emp)

print("\nExcellent (>=90):", excellent)
print("Good (75-89):", good)
print("Average (60-74):", average_list)
print("Poor (<60):", poor)
