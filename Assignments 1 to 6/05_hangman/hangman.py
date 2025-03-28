import random

word_list = ["python", "hangman", "developer", "programming", "computer", "software"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    print("🎮 Welcome to Hangman Game! 🔤")
    
    secret_word = choose_word()
    guessed_letters = set()
    attempts = 6  

    while attempts > 0:
        print("\nWord: " + display_word(secret_word, guessed_letters))
        print(f"❌ Wrong guesses left: {attempts}")
        
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed this letter!")
            continue
        
        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Good guess!")
            if set(secret_word) <= guessed_letters:
                print(f"🎉 Congratulations! You guessed the word: {secret_word}")
                break
        else:
            attempts -= 1
            print("❌ Wrong guess!")

    else:
        print(f"💀 Game Over! The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
