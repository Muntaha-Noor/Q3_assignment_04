def main():
    degree_fahrenheit = float(input("Enter temperature in Fahrenheit:"))

    degree_celsius = (degree_fahrenheit - 32) * 5.0 / 9.0
    
    print(f"Temperature: {degree_fahrenheit}F = {degree_celsius}C")
 
if __name__ == "__main__":
    main()