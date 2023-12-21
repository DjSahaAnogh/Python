import random

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player} and the computer chose {computer}.")
    if player == computer:
        print("It is a tie.")
    elif player == "papre":
        if computer == "rock":
            print("You win")
        else:
            print("You lose")
    elif player == "rock":
        if computer == "scissors":
            print("You win")
        else:
            print("You lose")
    elif player == "scissors":
        if computer == "paper":
            print("You win")
        else:
            print("You lose")


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
