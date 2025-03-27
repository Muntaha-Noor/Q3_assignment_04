GRAVITY_CONSTANTS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    try:
        earth_weight = float(input("Enter a weight on Earth: "))

        planet = input("Enter a planet: ")

        if planet in GRAVITY_CONSTANTS:
            planetary_weight = round(earth_weight * GRAVITY_CONSTANTS[planet], 2)
            print(f"The equivalent weight on {planet}: {planetary_weight}")
        else:
            print("Invalid planet name. Please enter a correct planet name.")

    except ValueError:
        print("Invalid input! Please enter a numeric weight.")

if __name__ == "__main__":
    main()
