PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Why don’t programmers like nature? It has too many bugs!"
SORRY: str = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT).strip()
    
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
