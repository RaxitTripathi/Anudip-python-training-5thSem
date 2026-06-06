'''Problem Statement 
A batsman's scores in different matches are stored in a list. 
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
Write a program to: 
• Count half-centuries and centuries.  
• Find the highest score.  
• Display all scores below 20.  
• Calculate the average score.  '''

scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Count half-centuries and centuries

half_century=0
century=0
for score in scores:
    if(score == 100):
        century += 1
    elif(score == 50):
        half_century +=1    

print("Total century:",century)
print("Total half century:",half_century)
# Find the highest score. 

highest_score=scores[0]
for score in scores:
    if(score > highest_score):
        highest_score=score
print("\nHighest score:",highest_score)

# Display all scores below 20. 
print("\nScores Below 20:")
print()
for score in scores:
    if(score < 20):
        print(score)

# Calculate the average score.

average_score=0
for score in scores:
    average_score += score

print("\nAverage score:",average_score/(len(scores)))
