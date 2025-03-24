import random

NUM_SIDES = 6

def main():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2

    print("Dice have", NUM_SIDES, "sides each.")
    print("Die 1 shows: ", die1)
    print("Die 2 shows: ", die2)
    print("Total of two dice: ", total)


if __name__ == "__main__":
    main()