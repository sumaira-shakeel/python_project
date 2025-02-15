# Project 2: Guess the number (Computer picks a number)
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)  # Computer selects a number
    guesses_left = 7  # Max guesses allowed

    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")

    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Skip to the next iteration
        
        # Checking the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the correct number in {7 - guesses_left + 1} tries.")
            return  # Exit the function when guessed correctly

        guesses_left -= 1  # Reduce guesses left

    # Only prints when the loop exits (all guesses used)
    print(f"\n❌ You ran out of guesses. The number was {number_to_guess}. Better luck next time!")

# Run the game
guess_the_number()
