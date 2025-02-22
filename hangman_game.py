import random

# Word list
words = ['enum', 'python', 'colab', 'vscode', 'game']
word = random.choice(words)

# Game variables
guessed_letters = []
attempts = 6

# Welcome message
print("Welcome to the Hangman game!")
print("_" * len(word))

# Main game loop
while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue  

    # Checking if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter, try another one!")
        continue

    guessed_letters.append(guess)  # Add guessed letter to list

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

    # Display current progress
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(display_word)

    # Check if the word is fully guessed
    if "_" not in display_word:
        print(f"Congratulations! The correct word is: {word}")
        break

# Game over message if attempts are finished
if attempts == 0:
    print(f"Game over! The correct word was: {word}")
