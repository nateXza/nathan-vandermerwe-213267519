import random
import string


def generate_password(length: int = 12, uppercase: bool = True, numbers: bool = True, symbols: bool = True) -> str:
    # Validate password length
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if uppercase else ''
    digits = string.digits if numbers else ''
    punctuation = string.punctuation if symbols else ''

    # Combine character sets based on user preferences
    all_characters = lowercase_letters + uppercase_letters + digits + punctuation

    # Ensure at least one character from each selected set is included
    password = []
    if uppercase:
        password.append(random.choice(uppercase_letters))
    if numbers:
        password.append(random.choice(digits))
    if symbols:
        password.append(random.choice(punctuation))

    # Fill the rest of the password with random characters
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def get_user_input():
    try:
        length = int(input("Enter password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4. Setting length to 4.")
            length = 4

        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        return length, uppercase, numbers, symbols
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
        return get_user_input()

if __name__ == "__main__":
    print("=== Password Generator ===")
    length, uppercase, numbers, symbols = get_user_input()

    password = generate_password(length, uppercase, numbers, symbols)
    print("\nGenerated Password:", password)