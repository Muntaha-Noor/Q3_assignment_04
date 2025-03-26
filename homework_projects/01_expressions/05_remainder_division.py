def main():

    dividend: int = int(input("please enter an interger to be divided: "))
    divisor: int = int(input("please enter an integer to divided by: "))

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    print(f"{dividend} divided by {divisor} is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
