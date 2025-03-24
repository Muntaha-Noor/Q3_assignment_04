def main():

    print("This program calculates the perimeter of a triangle.")

    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    perimeter = side1 + side2 + side3

    print("The perimeter of the traingle is: " + str(perimeter))

if __name__ == "__main__":
    main()