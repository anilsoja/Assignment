import random

rounds = 1
player_score = 0
computer_score = 0


def converted_choice(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"


while True:
    random_number = random.randint(1, 3)
    print("Select rock/paper/scissors:")
    player_choice = input()
    computer_choice = converted_choice(random_number)
    print("Computer Choice:", computer_choice)
    print("Player Choice:", player_choice)
    if player_choice == computer_choice:
        winner = "both"
    elif player_choice == "rock":
        if computer_choice == "scissors":
            player_score = player_score + 1
            winner = "player"
        else:
            computer_score = computer_score + 1
            winner = "computer"
    elif player_choice == "paper":
        if computer_choice == "rock":
            player_score = player_score + 1
            winner = "player"
        else:
            computer_score = computer_score + 1
            winner = "computer"
    elif player_choice == "scissors":
        if computer_choice == "paper":
            player_score = player_score + 1
            winner = "player"
        else:
            computer_score = computer_score + 1
            winner = "computer"

    history = {rounds: [player_choice, computer_choice, winner]}
    rounds = rounds + 1
    if rounds > 10:
        break
print("\n")
print("Score of player:", player_score)
print("Score of Computer:", computer_score)
if player_score > computer_score:
    print("Player Won")
else:
    print("Computer Won")

