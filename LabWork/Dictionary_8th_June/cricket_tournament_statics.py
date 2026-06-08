""" 4. Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs.  """

runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 

# 1. Display players scoring more than 500 runs. 

print("Players Scoring More Than 500 Runs:")
for player,score in runs.items():
    if(score >500):
        print(player)

# 2. Find the Orange Cap winner.  
orange_cap=0
orange_player=None
for player,score in runs.items():
    if(score > orange_cap):
        orange_cap=score
        orange_player=player

print("\nOrange Cap Winner: ",orange_player)

# 3. Find the lowest scorer. 

lowest_score=float("inf")
lowest_player=None

for player,score in runs.items():
    if(score < lowest_score):
        lowest_score=score
        lowest_player=player

print("\nLowest Scorer:",lowest_player)

# 4. Calculate total runs scored. 
total_runs=0
for player,score in runs.items():
    total_runs += score

print("\nTotal Tournament Runs:",total_runs)    

# 5. Create a list of players scoring below 400. 
print("\nPlayers Scoring Below 400: ")
below_400=[]
for player,score in runs.items():
    if score < 400:
        below_400.append(player)
print(below_400)

# Count players scoring between 400 and 600 runs.

between_400_600=0
for player,score in runs.items():
    if(score >400 and score<600):
        between_400_600 +=1
print("\nPlayers Between 400 and 600 Runs: ",between_400_600)      


""" output:

Players Scoring More Than 500 Runs:
Virat
Rohit
Gill
Pant

Orange Cap Winner:  Gill

Lowest Scorer: Hardik

Total Tournament Runs: 4657

Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja']

Players Between 400 and 600 Runs:  5 """