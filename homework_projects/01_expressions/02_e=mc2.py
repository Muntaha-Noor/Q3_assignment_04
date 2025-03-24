C: int = 299792458

def main():
    
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    energy_in_joules: float = mass_in_kg * (C ** 2)

    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + "Kg")
    print("C = " + str(C) + "m/s")
    
    print(str(energy_in_joules) + " Joules of energy")

if __name__ == "__main__":
    main()