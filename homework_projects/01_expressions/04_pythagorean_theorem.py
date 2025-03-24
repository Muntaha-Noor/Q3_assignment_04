import math

def main():

    ab: float = float(input("Enter length of side AB: "))
    ac: float = float(input("Enter length of side AC: "))

    bc: float = math.sqrt(ab ** 2 + ac ** 2)

    print("The length of BC (the hypotenuse) is: " + str(bc))

if __name__ == "__main__":
    main()