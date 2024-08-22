# Returns the nearest multiple of 4
def find_nearest_multiple(num):
    if num >= 4:
        nearest = num + (4 - (num % 4))
    else:
        nearest = 4
    return nearest

def game_over():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)
	
# Checks whether the numbers entered are consecutive
def are_numbers_consecutive(numbers):
    for i in range(1, len(numbers)):
        if (numbers[i] - numbers[i - 1]) != 1:
            return False
    return True

# Starts the 21 number game
def play_game():
    sequence = []
    last_number = 0
    while True:
        print("Enter 'F' to take the first turn.")
        print("Enter 'S' to take the second turn.")
        turn_choice = input('> ')
        
        # Player takes the first turn
        if turn_choice == "F":
            while True:
                if last_number == 20:
                    game_over()
                else:
                    print("\nYour Turn.")
                    print("\nHow many numbers do you wish to enter?")
                    user_input_count = int(input('> '))
                    
                    if 1 <= user_input_count <= 3:
                        computer_turn_count = 4 - user_input_count
                    else:
                        print("Invalid input. You are disqualified from the game.")
                        game_over()
            
                    print("Enter your numbers:")
                    for _ in range(user_input_count):
                        user_number = int(input('> '))
                        sequence.append(user_number)
                    
                    last_number = sequence[-1] 
                    
                    # Check if the input numbers are consecutive
                    if are_numbers_consecutive(sequence): 
                        if last_number == 21:
                            game_over()
                        else:
                            # Computer's turn
                            for j in range(1, computer_turn_count + 1):
                                sequence.append(last_number + j)
                            print("Sequence after computer's turn:")
                            print(sequence)
                            last_number = sequence[-1]
                    else:
                        print("\nYou did not enter consecutive integers.")
                        game_over()
                        
        # Player takes the second turn
        elif turn_choice == "S":
            computer_turn_count = 1
            last_number = 0
            while last_number < 20:
                # Computer's turn
                for j in range(1, computer_turn_count + 1):
                    sequence.append(last_number + j)
                print("Sequence after computer's turn:")
                print(sequence)
                if sequence[-1] == 20:
                    game_over()
                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you wish to enter?")
                    user_input_count = int(input('> '))
                    
                    print("Enter your numbers:")
                    for _ in range(user_input_count):
                        sequence.append(int(input('> ')))
                    
                    last_number = sequence[-1]
                    if are_numbers_consecutive(sequence):
                        nearest = find_nearest_multiple(last_number)
                        computer_turn_count = nearest - last_number
                        if computer_turn_count == 4:
                            computer_turn_count = 3
                    else:
                        print("\nYou did not enter consecutive integers.")
                        game_over()
            print("\n\nCONGRATULATIONS!!!")
            print("YOU WON!")
            exit(0)
            
        else:
            print("Invalid choice")
            
# Main loop to start the game
while True:
    print("Player 2 is the Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    start_game = input('> ')
    if start_game == 'Yes':
        play_game()
    else:
        print("Do you want to quit the game? (Yes / No)")
        quit_game = input('> ')
        if quit_game == "Yes":
            print("You are quitting the game...")
            exit(0)
        elif quit_game == "No":
            print("Continuing...")
        else:
            print("Invalid choice")
