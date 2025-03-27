MARS_GRAVITY = 0.378

def calculate_mars_weight(earth_weight: float) -> float:
    return round(earth_weight * MARS_GRAVITY, 2)

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    
    mars_weight = calculate_mars_weight(earth_weight)
    print(f"The equivalent weight on Mars: {mars_weight}")

if __name__ == "__main__":
    main()
