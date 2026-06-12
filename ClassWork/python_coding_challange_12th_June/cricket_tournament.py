""" Problem 7: Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament are given below. 
Sample Data 
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
1. Find the Orange Cap winner.  
2. Find the lowest scorer.  
3. Calculate total runs scored.  
4. Display players scoring more than 500 runs.  
5. Create a list of players scoring below 400.   """


#Given Data
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

""" 1. Find the Orange Cap winner.  
2. Find the lowest scorer.  
3. Calculate total runs scored. 
5. Create a list of players scoring below 400.
 """

orange_cap=0
orange_cap_player=""
lowest_score=float("inf")
lowest_scorer_player=""
total_run=0
player_below_400=[]

for player,run in runs.items():
    if run < 400:
        player_below_400.append(player)
    if run > orange_cap:
        orange_cap =run
        orange_cap_player =player
    elif run < lowest_score:
        lowest_score =run
        lowest_scorer_player=player
    total_run +=run        


print("Orange Cap Winner:",orange_cap_player)
print("Lowest Scorer:",lowest_scorer_player)
print("Total Run Scored:",total_run)

# 4. Display players scoring more than 500 runs.
print("\nPlayers Scoring Above 500:")
for player, run in runs.items():
    if run > 500:
        print(player)


# 5. Create a list of players scoring below 400.

print("\nPlayers Scoring Below 400:\n",player_below_400)

""" 
output:

Orange Cap Winner: Gill
Lowest Scorer: Hardik
Total Run Scored: 4657

Players Scoring Above 500:
Virat
Rohit
Gill
Pant

Players Scoring Below 400:
 ['Hardik', 'Surya', 'Jadeja'] """