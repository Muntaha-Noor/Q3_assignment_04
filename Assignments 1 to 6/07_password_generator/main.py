import random
import string

def generate_password(length=12):
    if length < 4:
        print("❌ Password length must be at least 4 characters!")
        return None

    uppercase_letters = string.ascii_uppercase  
    lowercase_letters = string.ascii_lowercase  
    digits = string.digits                      
    special_chars = string.punctuation          

    required_chars = random.choice(uppercase_letters) + \
                     random.choice(lowercase_letters) + \
                     random.choice(digits) + \
                     random.choice(special_chars)

    all_chars = uppercase_letters + lowercase_letters + digits + special_chars
    remaining_chars = "".join(random.choices(all_chars, k=length - 4))

    password = list(required_chars + remaining_chars)
    random.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    try:
        password_length = int(input("Enter password length: "))
        generated_password = generate_password(password_length)
        if generated_password:
            print(f"🔐 Your Secure Password: {generated_password}")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
