
import random
import string

def generate_password(length=12):
    # Define the character set: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    # Ask user for desired password length
    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        if length < 6:
            print("Password length should be at least 6 characters for security.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
