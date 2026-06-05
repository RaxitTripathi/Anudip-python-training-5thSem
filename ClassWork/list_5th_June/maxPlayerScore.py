

total_players=[] #List to store all player score
no_of_player=int(input("Enter no. of player:"))  #input no of player

for i in range(no_of_player):
    player_score=int(input("Enter player score:")) #input player score
    total_players.append(player_score)  #append to list

#max score
max_score=total_players[0]
player_number=0
for i in range(1,no_of_player):
    if(total_players[i] > max_score):
        max_score=total_players[i]
        player_number=i


print("Maximum score is:",max_score,"Of Player",player_number)        




