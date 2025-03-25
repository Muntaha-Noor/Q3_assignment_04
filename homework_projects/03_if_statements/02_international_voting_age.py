ZYPHORIA_AGE = 16
ELDORIA_AGE = 25
VERIDANIA_AGE = 48

def main():
    user_age = int(input("How old are you? "))

    if user_age >= ZYPHORIA_AGE:
        print(f"You can vote in Zyphoria where the voting age is {ZYPHORIA_AGE}.")
    else:
        print(f"You cannot vote in Zyphoria where the voting age is {ZYPHORIA_AGE}.")
    
    if user_age >= ELDORIA_AGE:
        print(f"You can vote in Eldoria where the voting age is {ELDORIA_AGE}.")
    else:
        print(f"You cannot vote in Eldoria where the voting age is {ELDORIA_AGE}.")
    
    if user_age >= VERIDANIA_AGE:
        print(f"You can vote in Veridania where the voting age is {VERIDANIA_AGE}.")
    else:
        print(f"You cannot vote in Veridania where the voting age is {VERIDANIA_AGE}.")

if __name__ == '__main__':
    main()
