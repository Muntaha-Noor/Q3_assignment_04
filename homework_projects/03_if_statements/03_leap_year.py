def main():
    # User se input lena
    year = int(input("Please input a year: "))

    # Leap year check karne ke liye conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Program run karne ke liye required line
if __name__ == '__main__':
    main()
