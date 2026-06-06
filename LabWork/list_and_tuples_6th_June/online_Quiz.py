'''Problem Statement 
Correct answers: 
correct = ['A', 'C', 'B', 'D', 'A'] 
Student answers: 
student = ['A', 'B', 'B', 'D', 'C'] 
Write a program to: 
• Calculate score.  
• Display incorrectly answered question numbers.  
• Count correct and wrong answers.  
• Determine pass/fail (minimum 60%). '''

# Correct and student answers
correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

correct_count = 0
wrong_count = 0

print("Incorrectly Answered Question Numbers:")

for i in range(len(correct)):
    if correct[i] == student[i]:
        correct_count += 1
    else:
        wrong_count += 1
        print(i + 1)

# Calculate score and percentage
score = correct_count
percentage = (correct_count / len(correct)) * 100

print("\nScore:", score, "out of", len(correct))
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)
print("Percentage:", percentage, "%")

# Pass/Fail
if percentage >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")