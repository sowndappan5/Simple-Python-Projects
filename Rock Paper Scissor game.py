import random

def print_instructions():
    """Print the winning rules of the game."""
    print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
          + "Rock vs Paper -> Paper wins\n"
          + "Rock vs Scissors -> Rock wins\n"
          + "Paper vs Scissors -> Scissors wins\n")

def get_user_choice():
    """Prompt the user for their choice and validate the input."""
    while True:
        try:
            choice = int(input("Enter your choice:\n1 - Rock\n2 - Paper\n3 - Scissors\n"))
            if choice in [1, 2, 3]:
                return choice
            else:
                print('Enter a valid choice (1, 2, or 3).')
        except ValueError:
            print('Invalid input. Please enter a number (1, 2, or 3).')

def get_computer_choice():
    """Randomly select a choice for the computer."""
    return random.randint(1, 3)

def choice_to_name(choice):
    """Convert choice number to name."""
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    else:
        return 'Scissors'

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "DRAW"
    elif (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 3) or \
         (user_choice == 3 and computer_choice == 1):
        return "Computer"
    else:
        return "User"

def play_game():
    """Main function to play the Rock-Paper-Scissors game."""
    print_instructions()

    while True:
        user_choice = get_user_choice()
        user_choice_name = choice_to_name(user_choice)
        print('User choice is:', user_choice_name)

        computer_choice = get_computer_choice()
        computer_choice_name = choice_to_name(computer_choice)
        print('Computer choice is:', computer_choice_name)

        winner = determine_winner(user_choice, computer_choice)
        if winner == "DRAW":
            print("<== It's a tie ==>")
        elif winner == "User":
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")

        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")

# Start the game
play_game()