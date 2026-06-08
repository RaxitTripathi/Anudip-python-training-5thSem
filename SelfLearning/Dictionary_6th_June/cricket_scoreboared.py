""" 4. Cricket Scoreboard Analysis 
Sample Data 
scores = { 
    "Virat": 78, 
    "Rohit": 112, 
    "Gill": 45, 
    "Rahul": 89, 
    "Hardik": 32, 
    "Jadeja": 61, 
    "Surya": 105, 
    "Pant": 95, 
    "Bumrah": 18, 
    "Shami": 25 
} 
Tasks 
• Display players who scored 50 or more runs.  
• Count the number of centuries.  
• Find the player with the highest score.  
• Create a list of players scoring below 30 runs.  
• Determine how many players scored between 50 and 99.  """

scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Players who scored 50 or more runs
print("Players who scored 50 or more runs:")
for player, score in scores.items():
    if score >= 50:
        print(player, ":", score)

# Count the number of centuries
centuries = 0
for score in scores.values():
    if score >= 100:
        centuries += 1
print("\nNumber of centuries:", centuries)

# Player with the highest score
highest_scorer = max(scores, key=scores.get)
print("\nHighest scorer:", highest_scorer)
print("Score:", scores[highest_scorer])

# List of players scoring below 30 runs
below_30 = []
for player, score in scores.items():
    if score < 30:
        below_30.append(player)

print("\nPlayers scoring below 30 runs:")
print(below_30)

# Players who scored between 50 and 99
count_50_99 = 0
for score in scores.values():
    if 50 <= score <= 99:
        count_50_99 += 1

print("\nPlayers scoring between 50 and 99 runs:", count_50_99)