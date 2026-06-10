# 1. Display all players
def display_players(players):
    for name in players:
        print(name, players[name])


# 2. Highest run scorer
def highest_runs(players):

    best = None

    for name in players:
        if best is None or players[name]["runs"] > players[best]["runs"]:
            best = name

    print("Highest Run Scorer:", best, players[best]["runs"])


# 3. Lowest run scorer
def lowest_runs(players):

    low = None

    for name in players:
        if low is None or players[name]["runs"] < players[low]["runs"]:
            low = name

    print("Lowest Run Scorer:", low, players[low]["runs"])


# 4. Average runs
def average_runs(players):

    total = 0

    for name in players:
        total += players[name]["runs"]

    avg = total / len(players)

    print("Average Runs =", round(avg, 2))


# 5. Max wickets
def max_wickets(players):

    best = None

    for name in players:
        if best is None or players[name]["wickets"] > players[best]["wickets"]:
            best = name

    print("Top Wicket Taker:", best, players[best]["wickets"])


# 6. All rounders
def all_rounders(players):

    for name in players:
        if players[name]["runs"] > 300 and players[name]["wickets"] > 5:
            print(name, players[name])


# 7. Above average batsmen
def above_average(players):

    total = 0

    for name in players:
        total += players[name]["runs"]

    avg = total / len(players)

    for name in players:
        if players[name]["runs"] > avg:
            print(name, players[name]["runs"])


# 8. Categories
def categories(players):

    print("\nPlayer Categories")

    for name in players:

        runs = players[name]["runs"]

        if runs >= 600:
            print(name, "Star Performer")

        elif runs >= 400:
            print(name, "Good Performer")

        elif runs >= 200:
            print(name, "Average Performer")

        else:
            print(name, "Poor Performer")


# 9. Team statistics
def team_stats(players):

    total_runs = 0
    total_wickets = 0

    for name in players:
        total_runs += players[name]["runs"]
        total_wickets += players[name]["wickets"]

    print("Team Runs =", total_runs)
    print("Team Wickets =", total_wickets)


# 10. Top 5 batsmen
def top_batsmen(players):

    sorted_players = sorted(players.items(), key=lambda x: x[1]["runs"], reverse=True)

    print("Top 5 Batsmen")

    for i in range(min(5, len(sorted_players))):
        print(sorted_players[i][0], sorted_players[i][1]["runs"])


# 11. Top 5 bowlers
def top_bowlers(players):

    sorted_players = sorted(players.items(), key=lambda x: x[1]["wickets"], reverse=True)

    print("Top 5 Bowlers")

    for i in range(min(5, len(sorted_players))):
        print(sorted_players[i][0], sorted_players[i][1]["wickets"])


# 12. Award winners
def award_winners(players):

    awards = {}

    for name in players:

        if players[name]["runs"] > 500 or players[name]["wickets"] > 10:
            awards[name] = players[name]

    print("Award Winners")

    for name in awards:
        print(name, awards[name])