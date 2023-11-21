import pyfiglet
from random import choice
from os import system, get_terminal_size


# Get player choice
def get_player_choice():
    while True:
        try:
            player_choice = input(
                "Please choose 'R'ock, 'P'aper or 'S'cissors "
            ).upper()
            if player_choice != "R" and player_choice != "P" and player_choice != "S":
                raise ValueError
        except ValueError:
            print("Invalid selection please try again")
        else:
            return player_choice


# Generate computer choice
def get_computer_choice():
    return choice(["R", "P", "S"])


def check_win(player, computer):
    if (
        player == "R"
        and computer == "R"
        or player == "P"
        and computer == "P"
        or player == "S"
        and computer == "S"
    ):
        win = "TIE"
    elif (
        player == "R"
        and computer == "S"
        or player == "P"
        and computer == "R"
        or player == "S"
        and computer == "P"
    ):
        win = "PLAYER WINS"
    else:
        win = "COMPUTER WINS"
    return win


def main():
    games_played = 0
    computer_score = 0
    player_score = 0
    ts = get_terminal_size().columns
    while True:
        # system('cls')
        print(
            pyfiglet.figlet_format(
                "Rock Paper Scissors", font="doom", justify="center", width=ts
            )
        )
        # print(ts)
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        win = check_win(player_choice, computer_choice)
        games_played += 1
        if win == "PLAYER WINS":
            player_score += 1
        elif win == "COMPUTER WINS":
            computer_score += 1
        print(f"player choice = {player_choice} computer choice = {computer_choice}")
        print(f"Result = {win}")
        print(f"CURRENT SCORE AFTER {games_played} GAMES PLAYED")
        print(f"PLAYER {player_score}")
        print(f"COMPUTER {computer_score}")


if __name__ == "__main__":
    main()

# Check winner and scores, first to 5 wins

# Ask to play again or finish
