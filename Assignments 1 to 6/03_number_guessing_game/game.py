import random

def computer_guesses():
    print("🖥️ Welcome to the Computer Guessing Game! 🎯")
    print("Think of a number between 1 and 100, and I'll try to guess it.")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = random.randint(low, high)
        attempts += 1

        print(f"\nIs it {guess}?")
        user_feedback = input("Enter 'H' if too high, 'L' if too low, or 'C' if correct: ").strip().upper()

        if user_feedback == 'C':
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts!")
            break
        elif user_feedback == 'H':
            high = guess - 1  
        elif user_feedback == 'L':
            low = guess + 1  
        else:
            print("❌ Invalid input! Please enter 'H' (High), 'L' (Low), or 'C' (Correct).")

if __name__ == "__main__":
    computer_guesses()
