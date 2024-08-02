import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.title_label = tk.Label(self.frame, text="Rock-Paper-Scissors", font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.frame)
        self.buttons_frame.pack(pady=10)

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=5)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=5)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.frame, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.frame, text=f"User: {self.user_score} | Computer: {self.computer_score}", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.frame, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def reset_game(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
