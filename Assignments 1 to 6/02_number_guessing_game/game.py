import random

def guess_the_number():
    print("🔢 Welcome to the Guess the Number Game! 🎯")
    print("I have selected a number between 1 and 100. Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  

        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 100.")

if __name__ == "__main__":
    guess_the_number()
