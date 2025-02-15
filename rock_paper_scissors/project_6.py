import random

# Available choices
choices = ["rock", "paper", "scissors"]

# Get player's choice
player = input("Enter your choice (rock, paper, scissors): ").strip().lower()

# Validate player input
if player not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    # Computer's random choice
    computer = random.choice(choices)

    # Display choices
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    # Game logic: Determine the winner
    if player == computer:
        print("It's a tie! 🤝")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("Congratulations! You win! 🚀")
    else:
        print("Oh no! The computer wins! 🖥️💀")

# Friendly end message
print("\nThanks for playing! Try again to test your luck. 🎮")
