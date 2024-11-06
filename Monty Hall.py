import numpy as np

def simulate_monty_hall(winning_door, initial_choice, switch=False):
    """
    Simulates a single round of the Monty Hall problem.
    
    Args:
        winning_door (int): The door hiding the prize (0, 1, or 2).
        initial_choice (int): The door initially chosen by the player (0, 1, or 2).
        switch (bool): Whether the player switches their choice after a non-winning door is revealed.
        
    Returns:
        bool: True if the player wins the prize, False otherwise.
    """
    assert 0 <= winning_door < 3, "winning_door must be 0, 1, or 2"
    assert 0 <= initial_choice < 3, "initial_choice must be 0, 1, or 2"

    # Presenter reveals a door that is neither the winning door nor the player's initial choice
    revealed_door = next(door for door in range(3) if door != initial_choice and door != winning_door)

    # If the player chooses to switch, change their choice to the remaining unrevealed door
    if switch:
        initial_choice = next(door for door in range(3) if door != initial_choice and door != revealed_door)

    # Return True if the player's final choice matches the winning door
    return initial_choice == winning_door


if __name__ == '__main__':
    # Simulate a large number of games
    num_simulations = 1_000_000
    player_choices = np.random.randint(0, 3, size=num_simulations)  # Random initial choices for each game

    # Calculate winning percentage without switching
    wins_without_switching = sum(simulate_monty_hall(winning_door=1, initial_choice=choice) for choice in player_choices)
    print("Winning percentage without switching choice:", wins_without_switching / num_simulations)

    # Calculate winning percentage with switching
    wins_with_switching = sum(simulate_monty_hall(winning_door=1, initial_choice=choice, switch=True) for choice in player_choices)
    print("Winning percentage while switching choice:", wins_with_switching / num_simulations)
