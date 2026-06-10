""" 4. Cricket Tournament Analytics System 
Problem Statement 
Store statistics of at least 30 cricket players. 
Example Structure 
players = { 
    "Virat": { 
        "runs": 645, 
        "matches": 12, 
        "wickets": 0 
    } 
} 
Requirements 
1. Display all player statistics.  
2. Find highest run scorer.  
3. Find lowest run scorer.  
4. Calculate average runs.  
5. Find player with maximum wickets.  
6. Find all-rounders (runs > 300 and wickets > 5).  
7. Display players scoring above average.  
8. Create categories:  
o Star Performer  
o Good Performer  
o Average Performer  
o Poor Performer  
9. Generate team statistics.  
10. Display top 5 batsmen.  
11. Display top 5 bowlers.  
12. Create a separate dictionary for award winners.  
Challenge 
Generate a tournament report. """

from cricket_tournaments_operation import *

players = {}

# 1. Input 30 players
print("Enter details of 30 players:\n")

for i in range(30):
    print(f"\nPlayer {i+1}")

    name = input("Enter Player Name: ")
    runs = int(input("Enter Runs: "))
    matches = int(input("Enter Matches: "))
    wickets = int(input("Enter Wickets: "))

    players[name] = {
        "runs": runs,
        "matches": matches,
        "wickets": wickets
    }

print("\nAll 30 players added successfully!")


# 2. Menu system
while True:

    print("\n----- CRICKET MENU -----")
    print("1. Display players")
    print("2. Highest run scorer")
    print("3. Lowest run scorer")
    print("4. Average runs")
    print("5. Top wicket taker")
    print("6. All rounders")
    print("7. Above average batsmen")
    print("8. Categories")
    print("9. Team stats")
    print("10. Top 5 batsmen")
    print("11. Top 5 bowlers")
    print("12. Award winners")
    print("13. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_players(players)

    elif choice == "2":
        highest_runs(players)

    elif choice == "3":
        lowest_runs(players)

    elif choice == "4":
        average_runs(players)

    elif choice == "5":
        max_wickets(players)

    elif choice == "6":
        all_rounders(players)

    elif choice == "7":
        above_average(players)

    elif choice == "8":
        categories(players)

    elif choice == "9":
        team_stats(players)

    elif choice == "10":
        top_batsmen(players)

    elif choice == "11":
        top_bowlers(players)

    elif choice == "12":
        award_winners(players)

    elif choice == "13":
        print("Exiting...")
        break

    else:
        print("Invalid choice")