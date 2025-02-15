import tkinter as tk
import random

# Function to play the game
def play(choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner
    if choice == computer_choice:
        result.set("It's a Tie! 🤝")
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result.set("You Win! 🎉")
    else:
        result.set("Computer Wins! 💻😈")

    player_choice.set(f"You: {choice}")
    comp_choice.set(f"Computer: {computer_choice}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="lightblue")

# Game labels
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)

player_choice = tk.StringVar()
comp_choice = tk.StringVar()
result = tk.StringVar()

tk.Label(root, textvariable=player_choice, font=("Arial", 14), bg="lightblue").pack()
tk.Label(root, textvariable=comp_choice, font=("Arial", 14), bg="lightblue").pack()
tk.Label(root, textvariable=result, font=("Arial", 16, "bold"), bg="lightblue", fg="red").pack(pady=10)

# Buttons for choices
tk.Button(root, text="Rock", font=("Arial", 14), command=lambda: play("Rock"), width=10, bg="white").pack(pady=5)
tk.Button(root, text="Paper", font=("Arial", 14), command=lambda: play("Paper"), width=10, bg="white").pack(pady=5)
tk.Button(root, text="Scissors", font=("Arial", 14), command=lambda: play("Scissors"), width=10, bg="white").pack(pady=5)

# Restart Button
tk.Button(root, text="Restart", font=("Arial", 12), command=lambda: result.set(""), width=10, bg="yellow").pack(pady=10)

# Run the application
root.mainloop()
