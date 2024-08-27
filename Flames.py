def remove_common_characters(char_list1, char_list2):
    """
    This function removes common characters from two lists of characters
    and returns a concatenated list along with a flag indicating if any
    common characters were found and removed.
    """
    for i in range(len(char_list1)):
        for j in range(len(char_list2)):
            # If a common character is found
            if char_list1[i] == char_list2[j]:
                common_char = char_list1[i]

                # Remove the common character from both lists
                char_list1.remove(common_char)
                char_list2.remove(common_char)

                # Concatenate the two lists with a border marker "*"
                combined_list = char_list1 + ["*"] + char_list2

                # Return the concatenated list with True flag
                return [combined_list, True]

    # If no common characters are found, return the concatenated list with False flag
    combined_list = char_list1 + ["*"] + char_list2
    return [combined_list, False]


# Driver code
if __name__ == "__main__":
    # Take first player's name
    player1 = input("Player 1 name: ")

    # Convert all letters to lower case and remove spaces
    player1 = player1.lower().replace(" ", "")
    player1_list = list(player1)

    # Take second player's name
    player2 = input("Player 2 name: ")
    player2 = player2.lower().replace(" ", "")
    player2_list = list(player2)

    # Initialize a flag to control the loop
    continue_processing = True

    # Keep calling remove_common_characters function until no common characters are found
    while continue_processing:
        # Call the function and store the returned value
        result_list = remove_common_characters(player1_list, player2_list)

        # Extract the concatenated list and the flag
        combined_list = result_list[0]
        continue_processing = result_list[1]

        # Find the index of the "*" border marker
        star_index = combined_list.index("*")

        # Perform list slicing
        player1_list = combined_list[:star_index]  # Characters before "*"
        player2_list = combined_list[star_index + 1:]  # Characters after "*"

    # Count the total remaining characters
    total_remaining = len(player1_list) + len(player2_list)

    # List of FLAMES acronyms
    flames_result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # Keep looping until only one item remains in the flames_result list
    while len(flames_result) > 1:
        # Calculate the index for slicing
        split_index = (total_remaining % len(flames_result) - 1)

        # Perform anticlockwise circular counting
        if split_index >= 0:
            right_part = flames_result[split_index + 1:]
            left_part = flames_result[:split_index]
            flames_result = right_part + left_part
        else:
            flames_result = flames_result[:len(flames_result) - 1]

    # Print the final relationship status
    print("Relationship status:", flames_result[0])