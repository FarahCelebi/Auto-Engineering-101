import random


def roll_die():
    """Rolls a die and returns a random number between 1 and 6."""
    return random.randint(1, 6)


def main():
    # Game setup
    board_length = 20  # Total length of the game board
    position = 0  # User's starting position on the board
    total_rolls = 5  # Total number of rolls allowed

    print("Welcome to the Dice Rolling Game!")
    print(f"Your goal is to reach space {board_length} on the board.")

    for roll_number in range(1, total_rolls + 1):
        # Roll the die
        roll = roll_die()
        print(f"\nRoll {roll_number}: You rolled a {roll}!")

        # Update user's position
        position += roll

        # Ensure the position does not exceed the board length
        if position > board_length:
            position = board_length

        # Calculate spaces remaining to win
        spaces_remaining = board_length - position

        # Display current status
        print(f"You are now on space {position}.")
        print(f"You need {spaces_remaining} more spaces to win.")

        # Check if user has won
        if position == board_length:
            print("\nCongratulations! You've reached the end of the board!")
            break
    else:
        # If loop completes without breaking, check if the user won or lost
        if position < board_length:
            print(f"\nGame over! You reached space {position}. Better luck next time!")
        else:
            print(f"\nCongratulations! You've reached the end of the board on roll {roll_number}!")


if __name__ == "__main__":
    main()