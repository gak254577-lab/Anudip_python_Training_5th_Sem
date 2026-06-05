print("-------- Welcome to the Football Game! --------")
num_players = int(input("Enter the number of players: "))
total_score = 0
for i in range (1, num_players + 1):
    player_name = input("Enter the name of player :")
    score = int(input("Enter the score of player :"))
    print("Player", i, ":", player_name, "Score:", score)
    total_score += score
print("Total Score:", total_score)

##    python -u "CLASSWORK_PYTHON/5thjune/Football_Game.py"