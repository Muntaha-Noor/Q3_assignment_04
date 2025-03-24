SENTENCE_START: str = "Once upon a time, there was a "

def main():

    adjective: str = input("Enter an adjective: ")
    noun: str = input("Enter a noun: ")
    verb: str = input("Enter a verb: ")

    print(SENTENCE_START + adjective + " " + noun + " accidentally " + verb + " into the government's pizza delivery system!")

if __name__ == "__main__":
    main()