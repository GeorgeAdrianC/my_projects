import random
    
"""A simple game of rock, paper, scissors"""


OPTIONS = ["rock", "paper", "scissors"]


def print_options():
    message = ""
    for index, option in enumerate(OPTIONS):
        message = message + f"({index + 1}) {option}\n"
    print(message)


def get_player_choice():
    while True:
        choice = input("Welcome to Rock, Paper, Scissors!\nEnter the number of your choice: ")
        try:
            choice_number = int(choice)
        except ValueError:
            print("Please input a integer")
            continue
        if choice_number not in [1, 2, 3]:
            print("Please input a number between 1 and 3")
            continue
        break
    return OPTIONS[choice_number - 1]


def get_computer_choice():
    return random.choice(OPTIONS)


def print_choices(player_choice, computer_choice):
    print(f"You chose {player_choice}")
    print(f"Computer chose {computer_choice}")


def print_win_lose(player_choice, computer_choice, player_beats, player_loses_to):
    if computer_choice == player_loses_to:
        print(f"Sorry, {computer_choice} beats {player_choice}")
    elif computer_choice == player_beats:
        print(f"Yes, {player_choice} beats {computer_choice}")


def print_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Draw!")
    elif player_choice == "rock":
        print_win_lose("rock", computer_choice, "scissors", "paper")
    elif player_choice == "paper":
        print_win_lose("paper", computer_choice, "rock", "scissors")
    elif player_choice == "scissors":
        print_win_lose("scissors", computer_choice, "paper", "rock")


print_options()
player_choice = get_player_choice()
computer_choice = get_computer_choice()
print_choices(player_choice, computer_choice)
print_result(player_choice, computer_choice)