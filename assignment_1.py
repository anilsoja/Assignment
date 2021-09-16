from random import randint

player_score = 0
computer_score = 0
choices = {}
c = {'rock': 0, 'paper': 1, 'scissors': 2}
d = ['rock', 'paper', 'scissors']

for i in range(1, 4):
    # outcomes = {
    #     "0": {"0": "0", "1": "1", "2": "-1"},  # 0: tie, 1: computer won, -1: player won
    #     "1": {"0": "-1", "1": "0", "2": "1"},
    #     "2": {"0": "1", "1": "-1", "2": "0"}
    # }
    outcomes = {0: {0: "Tie", 1: "Computer won", 2: "Player won"}, 1: {0: "Player won", 1: "Tie", 2: "Computer won"},
                2: {0: "Computer won", 1: "Player won", 2: "Tie"}}
    player_choice = input("Player Choice:")
    computer_choice = d[randint(0, 2)]
    print("Computer Choice:", computer_choice)
    print("Player Choice:", player_choice)
    if (c[player_choice] == 0 and c[computer_choice] == 2) or (c[player_choice] == 1 and c[computer_choice] == 0) or (
            c[player_choice] == 2 and c[computer_choice] == 1):
        player_score = player_score + 1
    else:
        if (c[player_choice] == 0 and c[computer_choice] == 1) or (
                c[player_choice] == 1 and c[computer_choice] == 2) or (
                c[player_choice] == 2 and c[computer_choice] == 0):
            computer_score = computer_score + 1
    result = outcomes[c[player_choice]][c[computer_choice]]
    choices[i] = [computer_choice, player_choice, result]
print(choices)
print("Player's score:", player_score, "and Computer's points:", computer_score)
if player_score > computer_score:
    print("Player is the winner")
elif player_score < computer_score:
    print("Computer is the winner")
else:
    print("It is a tie")
print("\n")

x = int(input("Enter the round for which you need the information >>"))
print("Player's's choice=", (choices[x][0]))
print("Computer's choice=", (choices[x][1]))
print(choices[x][2] + " round ", x)


