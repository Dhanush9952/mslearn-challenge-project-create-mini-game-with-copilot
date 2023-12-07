# Welcome message
print("Welcome to the Rock, Paper, Scissors minigame!")

# Initialize player and computer scores
player_score = 0
computer_score = 0

# Main game loop
while True:
    # Get player input
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Check for valid input
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid option. Please choose rock, paper, or scissors.")
        continue

    # Get computer's random choice
    # @TODO: Generate random choice for the computer (rock, paper, or scissors)
    # Get computer's random choice
    import random
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    # Get computer's random choice

    # Display player and computer choices
    print(f"Player chose: {player_choice}")
    print("Computer chose: @TODO")

    # Determine the winner of the round
    # @TODO: Determine winner based on player_choice and computer_choice
    # Update player_score and computer_score accordingly

    # Display the round result
    print("Round result: @TODO")

    # Display current scores
    print(f"Player Score: {player_score}, Computer Score: {computer_score}")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

# Display final scores
print("Game Over!")
print(f"Final Scores - Player: {player_score}, Computer: {computer_score}")
