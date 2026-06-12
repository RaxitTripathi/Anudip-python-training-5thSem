""" Problem 20: Employee Performance Evaluation System 
Problem Statement 
Employee performance scores are stored below. 
Sample Data 
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
5. Categorize employees:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60) 
 """



def employee_performance(performance):

    # Employees scoring above 80
    print("Employees Scoring Above 80:")
    for emp, score in performance.items():
        if score > 80:
            print(emp, ":", score)

    # Count employees needing improvement
    improvement_count = 0

    # Find top performer
    top_employee = ""
    top_score = 0

    total = 0

    print("\nEmployee Categories:")
    for emp, score in performance.items():

        total += score

        if score < 60:
            improvement_count += 1

        if score > top_score:
            top_score = score
            top_employee = emp

        # Categorization
        if score >= 90:
            category = "Excellent"
        elif score >= 75:
            category = "Good"
        elif score >= 60:
            category = "Average"
        else:
            category = "Poor"

        print(emp, ":", category)

    average = total / len(performance)

    print("\nEmployees Needing Improvement:", improvement_count)
    print("Top Performer:", top_employee, "Score:", top_score)
    print("Average Performance Score:", average)


try:
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

    if len(performance) == 0:
        raise ValueError("Performance data is empty.")

    employee_performance(performance)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)