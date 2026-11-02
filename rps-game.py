import random

OPTIONS = ["rock", "paper", "scissors"]


def get_user_information():
    name = input("What's your username? : ")

    while True:
        try:
            age = int(input("What's your age? : "))
            break
        except ValueError:
            print("Please enter a valid age.")

    return age, name


def get_computer_choice():
    return random.choice(OPTIONS)


def get_player_choice():
    choice = input("Enter a choice (rock, paper, scissors): ").lower()
    if choice in OPTIONS:
        return choice
    print("Please put a valid choice.")
    return get_player_choice()


def the_difficulty(age, name):
    print(f"Welcome {name}!")
    if age <= 9:
        print("The difficulty has been set to Easy!")
    elif age <= 18:
        print("The difficulty has been set to Meduim!")
    else:
        print("The difficulty has been set to Hard!")


def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"

    win_conditions = [
        (player == "rock" and computer == "scissors"),
        (player == "paper" and computer == "rock"),
        (player == "scissors" and computer == "paper")
    ]

    if any(win_conditions):
        return "The Player Has won!"

    return "The AI has won!"


def play_game():
    player = get_player_choice()
    computer = get_computer_choice()

    print(f"You chose: {player}, Computer chose: {computer}")

    result = determine_winner(player, computer)
    print(result)


age, name = get_user_information()
the_difficulty(age, name)

if __name__ == "__main__":
    play_game()
