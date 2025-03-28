import random

def get_computer_choice():
    """Randomly selects Rock, Paper, or Scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the choices."""
    if user_choice == computer_choice:
        return "🤝 It's a tie!"
    
    winning_combinations = {
        "rock": "scissors",  
        "scissors": "paper",  
        "paper": "rock"      
    }

    if winning_combinations[user_choice] == computer_choice:
        return "🎉 You win!"
    else:
        return "😞 You lose!"

def rock_paper_scissors():
    """Runs the Rock, Paper, Scissors game."""
    print("🎮 Welcome to Rock, Paper, Scissors Game! ✊✋✌️")
    
    while True:
        user_choice = input("\nEnter Rock, Paper, or Scissors (or 'quit' to exit): ").strip().lower()

        if user_choice == "quit":
            print("👋 Thanks for playing! Goodbye!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"🖥️ Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    rock_paper_scissors()
